"""
Base Solution Class
==================

Provides common functionality for all DSA solutions including
testing, benchmarking, and performance analysis.
"""

import os
import sys
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils.benchmarking.performance_analyzer import PerformanceAnalyzer
from utils.testing.test_runner import TestRunner


@dataclass
class TestCase:
    """Standard test case structure"""

    input: Any
    expected: Any
    description: str = ""
    timeout: float = 1.0  # seconds


class BaseSolution(ABC):
    """
    Base class for all DSA solutions

    Subclasses only need to implement the solve() method.
    All testing, benchmarking, and analysis is handled automatically.
    """

    def __init__(self, problem_name: str = None):
        self.problem_name = problem_name or self.__class__.__name__
        self.test_runner = TestRunner()
        self.performance_analyzer = PerformanceAnalyzer()
        self.test_cases: List[TestCase] = []

    @abstractmethod
    def solve(self, *args, **kwargs) -> Any:
        """
        Main solution method - must be implemented by subclasses

        Args:
            *args: Input arguments for the problem
            **kwargs: Additional keyword arguments

        Returns:
            Solution result
        """
        pass

    def solve_optimized(self, *args, **kwargs) -> Any:
        """
        Optimized solution method - override if you have a better approach
        Defaults to the main solve() method
        """
        return self.solve(*args, **kwargs)

    def load_test_cases(self, test_file: str = None) -> List[TestCase]:
        """
        Load test cases from TOML file or return default test cases

        Args:
            test_file: Path to TOML test file (optional)

        Returns:
            List of TestCase objects
        """
        if test_file and os.path.exists(test_file):
            return self._load_test_cases_from_file(test_file)
        else:
            return self._get_default_test_cases()

    def _load_test_cases_from_file(self, test_file: str) -> List[TestCase]:
        """Load test cases from TOML file"""
        try:
            import toml

            with open(test_file, "r") as f:
                data = toml.load(f)

            test_cases = []
            for test_data in data.get("test_cases", []):
                # Handle different input formats
                if "target" in test_data:
                    # For problems like Two Sum with separate input and target
                    input_data = (test_data["input"], test_data["target"])
                elif "l1" in test_data and "l2" in test_data:
                    # For problems like Add Two Numbers with two lists
                    input_data = (test_data["l1"], test_data["l2"])
                else:
                    # For other problems with single input
                    input_data = test_data["input"]

                test_case = TestCase(
                    input=input_data,
                    expected=test_data["expected"],
                    description=test_data.get("description", ""),
                    timeout=test_data.get("timeout", 1.0),
                )
                test_cases.append(test_case)

            return test_cases
        except ImportError:
            print("Warning: TOML not available, using default test cases")
            return self._get_default_test_cases()
        except Exception as e:
            print(f"Error loading test cases: {e}")
            return self._get_default_test_cases()

    def _get_default_test_cases(self) -> List[TestCase]:
        """Override this method to provide default test cases"""
        return []

    def run_tests(self, test_cases: List[TestCase] = None) -> List[Any]:
        """Run tests and return results"""
        if test_cases is None:
            test_cases = self.test_cases

        if not test_cases:
            print("No test cases available")
            return []

        print(f"🧪 Testing {self.problem_name}")
        print("=" * 50)

        results = self.test_runner.run_tests(self, test_cases)
        return results

    def run_performance_analysis(self, test_cases: List[TestCase] = None) -> Dict[str, Any]:
        """Run performance analysis and return results"""
        if test_cases is None:
            test_cases = self.test_cases

        if not test_cases:
            print("No test cases available for performance analysis")
            return {}

        print(f"\n📊 Performance Analysis for {self.problem_name}")
        print("=" * 50)

        results = self.performance_analyzer.analyze(self, test_cases)
        return results

    def run_benchmark(self, test_cases: List[TestCase] = None) -> Dict[str, Any]:
        """Run performance benchmark comparing solve() vs solve_optimized()"""
        if test_cases is None:
            test_cases = self.test_cases

        if not test_cases:
            print("No test cases available for benchmarking")
            return {}

        print(f"\n⚡ Benchmarking {self.problem_name}")
        print("=" * 50)

        # Test main solution
        print("Testing main solution...")
        main_times = []
        for test_case in test_cases:
            start_time = time.time()
            if isinstance(test_case.input, (list, tuple)):
                result = self.solve(*test_case.input)
            else:
                result = self.solve(test_case.input)
            execution_time = time.time() - start_time
            main_times.append(execution_time)

        # Test optimized solution
        print("Testing optimized solution...")
        opt_times = []
        for test_case in test_cases:
            start_time = time.time()
            if isinstance(test_case.input, (list, tuple)):
                result = self.solve_optimized(*test_case.input)
            else:
                result = self.solve_optimized(test_case.input)
            execution_time = time.time() - start_time
            opt_times.append(execution_time)

        # Calculate metrics
        avg_main = sum(main_times) / len(main_times)
        avg_opt = sum(opt_times) / len(opt_times)
        speedup = avg_main / avg_opt if avg_opt > 0 else 0

        print(f"\n📈 Benchmark Results:")
        print(f"Main solution average: {avg_main:.6f}s")
        print(f"Optimized solution average: {avg_opt:.6f}s")
        print(f"Speedup: {speedup:.2f}x")

        return {
            "main_times": main_times,
            "opt_times": opt_times,
            "avg_main": avg_main,
            "avg_opt": avg_opt,
            "speedup": speedup,
        }

    def run_all(self, test_cases: List[TestCase] = None):
        """Run all tests, analysis, and benchmarks"""
        if test_cases is None:
            test_cases = self.test_cases

        if not test_cases:
            print("No test cases available")
            return

        # Run tests
        self.run_tests(test_cases)

        # Run performance analysis
        self.run_performance_analysis(test_cases)

        # Run benchmark
        self.run_benchmark(test_cases)

    def interactive_mode(self):
        """Interactive mode for manual testing with enhanced features"""
        print(f"\n🎮 Interactive Mode - {self.problem_name}")
        print("=" * 50)
        self._show_interactive_help()

        while True:
            try:
                user_input = input("\n> ").strip()

                # Handle exit commands
                if user_input.lower() in ["quit", "exit", "q"]:
                    print("👋 Goodbye!")
                    break

                # Handle empty input
                if not user_input:
                    continue

                # Handle special commands
                if user_input.lower() in ["help", "h", "?"]:
                    self._show_interactive_help()
                    continue
                elif user_input.lower() in ["test", "tests", "t"]:
                    self._show_test_cases_menu()
                    continue
                elif user_input.lower() in ["run", "r"]:
                    self._run_all_tests_interactive()
                    continue
                elif user_input.lower() in ["benchmark", "bench", "b"]:
                    self._run_benchmark_interactive()
                    continue
                elif user_input.lower() in ["analyze", "analysis", "a"]:
                    self._run_analysis_interactive()
                    continue

                # Handle test case selection (e.g., "test 1", "t 3")
                if user_input.lower().startswith(("test ", "t ")):
                    try:
                        test_num = int(user_input.split()[1])
                        self._run_specific_test(test_num - 1)  # Convert to 0-based index
                        continue
                    except (ValueError, IndexError):
                        print("❌ Invalid test number. Use 'test 1', 'test 2', etc.")
                        continue

                # Handle regular input parsing
                parsed_input = self._parse_interactive_input(user_input)

                if parsed_input is None:
                    print("❌ Invalid input format")
                    print(
                        "💡 Type 'help' for available commands or check the "
                        "_parse_interactive_input method"
                    )
                    continue

                # Run both solutions
                self._run_solutions_comparison(parsed_input)

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! (Ctrl+C)")
                break
            except EOFError:
                print("\n\n👋 Goodbye! (Ctrl+D)")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

    def _show_interactive_help(self):
        """Show interactive mode help"""
        print("\n📋 Available Commands:")
        print("  help, h, ?     - Show this help")
        print("  test, tests, t - List available test cases")
        print("  test N         - Run specific test case (e.g., 'test 1')")
        print("  run, r         - Run all test cases")
        print("  benchmark, b   - Run performance benchmark")
        print("  analyze, a     - Run performance analysis")
        print("  quit, exit, q  - Exit interactive mode")
        print("  Ctrl+C, Ctrl+D - Exit interactive mode")
        print("\n💡 Or enter your custom input directly")
        print("💡 Check the _parse_interactive_input method for expected format")

    def _show_test_cases_menu(self):
        """Show available test cases from TOML file"""
        if not self.test_cases:
            print("❌ No test cases available")
            return

        print(f"\n📝 Available Test Cases ({len(self.test_cases)} total):")
        print("-" * 60)
        for i, test_case in enumerate(self.test_cases, 1):
            print(f"  {i:2d}. {test_case.description}")
            if hasattr(test_case, "input") and test_case.input:
                if isinstance(test_case.input, tuple):
                    print(f"      Input: {test_case.input}")
                else:
                    print(f"      Input: {test_case.input}")
                print(f"      Expected: {test_case.expected}")
            print()

        print("💡 Use 'test N' to run a specific test case")

    def _run_specific_test(self, test_index: int):
        """Run a specific test case by index"""
        if not self.test_cases or test_index < 0 or test_index >= len(self.test_cases):
            print(f"❌ Invalid test number. Available: 1-{len(self.test_cases)}")
            return

        test_case = self.test_cases[test_index]
        print(f"\n🧪 Running Test {test_index + 1}: {test_case.description}")
        print("-" * 50)

        # Run the test
        result = self.test_runner.run_single_test(self, test_case)

        if result.passed:
            print(
                f"✅ PASSED ({result.execution_time:.6f}s, "
                f"{result.memory_usage / 1024 / 1024:.2f}MB)"
            )
        else:
            print(
                f"❌ FAILED ({result.execution_time:.6f}s, "
                f"{result.memory_usage / 1024 / 1024:.2f}MB)"
            )
            if result.error_message:
                print(f"   Error: {result.error_message}")

    def _run_all_tests_interactive(self):
        """Run all test cases in interactive mode"""
        if not self.test_cases:
            print("❌ No test cases available")
            return

        print(f"\n🧪 Running All Tests ({len(self.test_cases)} total)")
        print("=" * 50)
        self.run_tests(self.test_cases)

    def _run_benchmark_interactive(self):
        """Run benchmark in interactive mode"""
        if not self.test_cases:
            print("❌ No test cases available")
            return

        print(f"\n⚡ Running Benchmark")
        print("=" * 50)
        self.run_benchmark(self.test_cases)

    def _run_analysis_interactive(self):
        """Run performance analysis in interactive mode"""
        if not self.test_cases:
            print("❌ No test cases available")
            return

        print(f"\n📊 Running Performance Analysis")
        print("=" * 50)
        self.run_performance_analysis(self.test_cases)

    def _run_solutions_comparison(self, parsed_input):
        """Run both solutions and compare results"""
        try:
            start_time = time.time()
            result1 = (
                self.solve(*parsed_input)
                if isinstance(parsed_input, tuple)
                else self.solve(parsed_input)
            )
            time1 = time.time() - start_time

            start_time = time.time()
            result2 = (
                self.solve_optimized(*parsed_input)
                if isinstance(parsed_input, tuple)
                else self.solve_optimized(parsed_input)
            )
            time2 = time.time() - start_time

            print(f"Main solution: {result1} ({time1:.6f}s)")
            print(f"Optimized:    {result2} ({time2:.6f}s)")

            if result1 == result2:
                print("✅ Both solutions agree!")
            else:
                print("❌ Solutions disagree!")

        except Exception as e:
            print(f"❌ Error running solutions: {e}")

    def _parse_interactive_input(self, user_input: str) -> Any:
        """Parse interactive input - override for custom parsing"""
        # Default implementation - subclasses should override
        return user_input


def main_solution_runner(solution_class, test_file: str = None):
    """
    Decorator/helper function to run a solution with all features

    Usage:
        if __name__ == "__main__":
            main_solution_runner(TwoSum, "test_cases.toml")
    """
    solution = solution_class()

    # Load test cases
    if test_file:
        solution.test_cases = solution.load_test_cases(test_file)
    else:
        solution.test_cases = solution.load_test_cases()

    # Run everything
    solution.run_all()

    # Interactive mode
    solution.interactive_mode()
