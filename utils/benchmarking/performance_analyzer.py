"""
Performance Analyzer Module
===========================

Provides comprehensive performance analysis for DSA solutions
including time complexity analysis, memory profiling, and optimization suggestions.
"""

import sys
import time
import tracemalloc
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import psutil
from memory_profiler import profile


@dataclass
class PerformanceMetrics:
    """Performance metrics for a solution"""

    execution_time: float
    memory_usage: float
    time_complexity: str
    space_complexity: str
    cpu_usage: float
    peak_memory: float


class PerformanceAnalyzer:
    """Comprehensive performance analyzer"""

    def __init__(self):
        self.metrics_history: List[PerformanceMetrics] = []
        self.test_sizes = [10, 50, 100, 500, 1000, 5000, 10000]

    def analyze_time_complexity(self, solution: Any, test_cases: List[Any]) -> str:
        """Analyze time complexity by running tests with different input sizes"""
        if not test_cases:
            return "Unknown - No test cases provided"

        # Generate test cases with different sizes
        execution_times = []
        input_sizes = []

        for size in self.test_sizes:
            # Create test case with given size
            test_input = self._generate_test_input(test_cases[0], size)

            # Measure execution time
            start_time = time.time()
            try:
                if isinstance(test_input, (list, tuple)):
                    solution.solve(*test_input)
                else:
                    solution.solve(test_input)
                execution_time = time.time() - start_time
                execution_times.append(execution_time)
                input_sizes.append(size)
            except Exception as e:
                print(f"Error testing size {size}: {e}")
                break

        if len(execution_times) < 2:
            return "Unknown - Insufficient data"

        # Analyze growth pattern
        complexity = self._analyze_growth_pattern(input_sizes, execution_times)
        return complexity

    def analyze_space_complexity(self, solution: Any, test_cases: List[Any]) -> str:
        """Analyze space complexity using memory profiling"""
        if not test_cases:
            return "Unknown - No test cases provided"

        # Use tracemalloc for precise memory tracking
        tracemalloc.start()

        try:
            # Run solution
            test_input = test_cases[0].input if hasattr(test_cases[0], "input") else test_cases[0]
            if isinstance(test_input, (list, tuple)):
                solution.solve(*test_input)
            else:
                solution.solve(test_input)

            # Get memory usage
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Analyze space complexity based on input size
            input_size = self._get_input_size(test_input)
            if input_size > 0:
                space_per_element = peak / input_size
                if space_per_element < 10:  # bytes
                    return "O(1)"
                elif space_per_element < 1000:  # bytes
                    return "O(n)"
                else:
                    return "O(n²) or higher"
            else:
                return "Unknown - Cannot determine input size"

        except Exception as e:
            tracemalloc.stop()
            return f"Error analyzing space complexity: {e}"

    def analyze(self, solution: Any, test_cases: List[Any]) -> Dict[str, Any]:
        """Run comprehensive performance analysis"""
        print("Running performance analysis...")
        print("=" * 50)

        # Time complexity analysis
        print("Analyzing time complexity...")
        time_complexity = self.analyze_time_complexity(solution, test_cases)
        print(f"Time Complexity: {time_complexity}")

        # Space complexity analysis
        print("\nAnalyzing space complexity...")
        space_complexity = self.analyze_space_complexity(solution, test_cases)
        print(f"Space Complexity: {space_complexity}")

        # Memory profiling
        print("\nRunning memory profiling...")
        memory_metrics = self._profile_memory(solution, test_cases)

        # CPU profiling
        print("\nAnalyzing CPU usage...")
        cpu_metrics = self._profile_cpu(solution, test_cases)

        # Generate performance report
        analysis_results = {
            "time_complexity": time_complexity,
            "space_complexity": space_complexity,
            "memory_metrics": memory_metrics,
            "cpu_metrics": cpu_metrics,
            "optimization_suggestions": self._generate_optimization_suggestions(
                time_complexity, space_complexity, memory_metrics, cpu_metrics
            ),
        }

        # Print summary
        self._print_analysis_summary(analysis_results)

        return analysis_results

    def _generate_test_input(self, base_test_case: Any, size: int) -> Any:
        """Generate test input of specified size"""
        if hasattr(base_test_case, "input"):
            base_input = base_test_case.input
        else:
            base_input = base_test_case

        # Simple size scaling - override for specific problem types
        if isinstance(base_input, list):
            return list(range(size))
        elif isinstance(base_input, str):
            return str(size)
        else:
            return base_input

    def _get_input_size(self, test_input: Any) -> int:
        """Get the size of the input for complexity analysis"""
        if isinstance(test_input, (list, tuple)):
            return len(test_input)
        elif isinstance(test_input, str):
            return len(test_input)
        elif isinstance(test_input, (int, float)):
            return int(test_input)
        else:
            return 1

    def _analyze_growth_pattern(self, sizes: List[int], times: List[float]) -> str:
        """Analyze the growth pattern to determine time complexity"""
        if len(sizes) < 2:
            return "Unknown"

        # Calculate ratios
        size_ratios = [sizes[i] / sizes[i - 1] for i in range(1, len(sizes))]
        time_ratios = [
            times[i] / times[i - 1] if times[i - 1] > 0 else 1.0 for i in range(1, len(times))
        ]

        # Analyze growth pattern
        avg_time_ratio = sum(time_ratios) / len(time_ratios)
        avg_size_ratio = sum(size_ratios) / len(size_ratios)

        if avg_time_ratio < 1.5:
            return "O(1) - Constant time"
        elif avg_time_ratio < avg_size_ratio * 1.5:
            return "O(log n) - Logarithmic time"
        elif avg_time_ratio < avg_size_ratio * 2:
            return "O(n) - Linear time"
        elif avg_time_ratio < avg_size_ratio * 3:
            return "O(n log n) - Linearithmic time"
        elif avg_time_ratio < avg_size_ratio * 4:
            return "O(n²) - Quadratic time"
        else:
            return f"O(n^k) where k > 2 - Higher order polynomial"

    def _profile_memory(self, solution: Any, test_cases: List[Any]) -> Dict[str, float]:
        """Profile memory usage"""
        if not test_cases:
            return {}

        tracemalloc.start()

        try:
            test_input = test_cases[0].input if hasattr(test_cases[0], "input") else test_cases[0]
            if isinstance(test_input, (list, tuple)):
                solution.solve(*test_input)
            else:
                solution.solve(test_input)

            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            return {
                "current_memory_mb": current / 1024 / 1024,
                "peak_memory_mb": peak / 1024 / 1024,
                "memory_delta_mb": (peak - current) / 1024 / 1024,
            }
        except Exception as e:
            tracemalloc.stop()
            return {"error": str(e)}

    def _profile_cpu(self, solution: Any, test_cases: List[Any]) -> Dict[str, float]:
        """Profile CPU usage"""
        if not test_cases:
            return {}

        process = psutil.Process()
        start_cpu = process.cpu_percent()

        try:
            test_input = test_cases[0].input if hasattr(test_cases[0], "input") else test_cases[0]
            if isinstance(test_input, (list, tuple)):
                solution.solve(*test_input)
            else:
                solution.solve(test_input)

            end_cpu = process.cpu_percent()
            return {
                "start_cpu_percent": start_cpu,
                "end_cpu_percent": end_cpu,
                "cpu_delta": end_cpu - start_cpu,
            }
        except Exception as e:
            return {"error": str(e)}

    def _generate_optimization_suggestions(
        self,
        time_comp: str,
        space_comp: str,
        memory_metrics: Dict,
        cpu_metrics: Dict,
    ) -> List[str]:
        """Generate optimization suggestions based on analysis"""
        suggestions = []

        # Time complexity suggestions
        if "O(n²)" in time_comp or "O(n^k)" in time_comp:
            suggestions.append("Consider using more efficient algorithms (e.g., sorting, hashing)")
            suggestions.append("Look for opportunities to reduce nested loops")

        if "O(2^n)" in time_comp or "exponential" in time_comp.lower():
            suggestions.append("Consider dynamic programming or memoization")
            suggestions.append("Look for overlapping subproblems")

        # Space complexity suggestions
        if "O(n²)" in space_comp or "higher" in space_comp:
            suggestions.append("Consider in-place algorithms to reduce space usage")
            suggestions.append("Use iterative approaches instead of recursive when possible")

        # Memory usage suggestions
        if memory_metrics.get("peak_memory_mb", 0) > 100:
            suggestions.append("High memory usage detected - consider optimizing data structures")

        # CPU usage suggestions
        if cpu_metrics.get("cpu_delta", 0) > 80:
            suggestions.append("High CPU usage detected - consider algorithmic optimizations")

        return suggestions

    def _print_analysis_summary(self, results: Dict[str, Any]):
        """Print a summary of the analysis results"""
        print("\n" + "=" * 50)
        print("PERFORMANCE ANALYSIS SUMMARY")
        print("=" * 50)

        print(f"Time Complexity: {results['time_complexity']}")
        print(f"Space Complexity: {results['space_complexity']}")

        if "memory_metrics" in results and results["memory_metrics"]:
            mem = results["memory_metrics"]
            if "peak_memory_mb" in mem:
                print(f"Peak Memory Usage: {mem['peak_memory_mb']:.2f} MB")

        if "cpu_metrics" in results and results["cpu_metrics"]:
            cpu = results["cpu_metrics"]
            if "cpu_delta" in cpu:
                print(f"CPU Usage: {cpu['cpu_delta']:.1f}%")

        if results["optimization_suggestions"]:
            print("\nOptimization Suggestions:")
            for i, suggestion in enumerate(results["optimization_suggestions"], 1):
                print(f"  {i}. {suggestion}")

        print("=" * 50)
