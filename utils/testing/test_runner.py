"""
Test Runner Module
==================

Provides comprehensive testing capabilities for DSA solutions
including timeout detection, memory profiling, and performance analysis.
"""

import os
import subprocess
import sys
import time
import traceback
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Callable, Dict, List

import psutil


@dataclass
class TestResult:
    """Test execution result"""

    test_case: Any
    passed: bool
    actual_output: Any
    expected_output: Any
    execution_time: float
    memory_usage: float
    error_message: str = ""
    timeout_occurred: bool = False


class TestRunner:
    """Comprehensive test runner with performance analysis"""

    def __init__(self, timeout: float = 5.0, memory_limit: int = 512):  # MB
        self.timeout = timeout
        self.memory_limit = memory_limit * 1024 * 1024  # Convert to bytes
        self.results: List[TestResult] = []

    @contextmanager
    def resource_monitor(self):
        """Context manager to monitor resource usage"""
        process = psutil.Process()
        start_memory = process.memory_info().rss
        start_time = time.time()

        try:
            yield
        finally:
            end_time = time.time()
            end_memory = process.memory_info().rss
            self.last_execution_time = end_time - start_time
            self.last_memory_usage = end_memory - start_memory

    def run_single_test(self, solution: Any, test_case: Any) -> TestResult:
        """Run a single test case with monitoring"""
        start_time = time.time()
        actual_output = None
        error_message = ""
        timeout_occurred = False
        memory_usage = 0

        try:
            with self.resource_monitor():
                # Set up timeout
                if hasattr(test_case, "timeout"):
                    timeout = test_case.timeout
                else:
                    timeout = self.timeout

                # Run the solution
                if hasattr(test_case, "input"):
                    if isinstance(test_case.input, (list, tuple)):
                        actual_output = solution.solve(*test_case.input)
                    else:
                        actual_output = solution.solve(test_case.input)
                else:
                    actual_output = solution.solve()

                execution_time = time.time() - start_time
                memory_usage = getattr(self, "last_memory_usage", 0)

                # Check timeout
                if execution_time > timeout:
                    timeout_occurred = True
                    error_message = f"Timeout exceeded: {execution_time:.3f}s > {timeout}s"

                # Check memory limit
                if memory_usage > self.memory_limit:
                    error_message += f" Memory limit exceeded: {memory_usage / 1024 / 1024:.2f}MB"

        except Exception as e:
            execution_time = time.time() - start_time
            error_message = str(e)
            traceback.print_exc()

        # Determine if test passed
        expected = getattr(test_case, "expected", None)
        passed = not timeout_occurred and not error_message and actual_output == expected

        if not passed and not error_message and expected is not None:
            error_message = f"Expected: {expected}, Got: {actual_output}"

        return TestResult(
            test_case=test_case,
            passed=passed,
            actual_output=actual_output,
            expected_output=expected,
            execution_time=execution_time,
            memory_usage=memory_usage,
            error_message=error_message,
            timeout_occurred=timeout_occurred,
        )

    def run_tests(self, solution: Any, test_cases: List[Any]) -> List[TestResult]:
        """Run all test cases and return results"""
        print(f"Running {len(test_cases)} test cases...")
        print("-" * 50)

        self.results = []

        for i, test_case in enumerate(test_cases, 1):
            print(f"Test {i}: {getattr(test_case, 'description', 'No description')}")

            result = self.run_single_test(solution, test_case)
            self.results.append(result)

            # Print result
            if result.passed:
                print(
                    f"  ✓ PASSED ({result.execution_time:.3f}s, "
                    f"{result.memory_usage / 1024 / 1024:.2f}MB)"
                )
            else:
                print(
                    f"  ✗ FAILED ({result.execution_time:.3f}s, "
                    f"{result.memory_usage / 1024 / 1024:.2f}MB)"
                )
                if result.error_message:
                    print(f"    Error: {result.error_message}")
                if result.timeout_occurred:
                    print(
                        f"    Timeout: {result.execution_time:.3f}s > "
                        f"{getattr(test_case, 'timeout', self.timeout)}s"
                    )

            print()

        # Summary
        passed_count = sum(1 for r in self.results if r.passed)
        total_count = len(self.results)
        print(f"Results: {passed_count}/{total_count} tests passed")

        if passed_count < total_count:
            print("\nFailed tests:")
            for i, result in enumerate(self.results, 1):
                if not result.passed:
                    print(
                        f"  {i}. " f"{getattr(result.test_case, 'description', 'No description')}"
                    )
                    if result.error_message:
                        print(f"     {result.error_message}")

        return self.results

    def get_performance_summary(self) -> Dict[str, float]:
        """Get performance summary statistics"""
        if not self.results:
            return {}

        execution_times = [r.execution_time for r in self.results]
        memory_usages = [r.memory_usage for r in self.results]

        return {
            "avg_execution_time": sum(execution_times) / len(execution_times),
            "max_execution_time": max(execution_times),
            "min_execution_time": min(execution_times),
            "avg_memory_usage": sum(memory_usages) / len(memory_usages),
            "max_memory_usage": max(memory_usages),
            "min_memory_usage": min(memory_usages),
            "total_tests": len(self.results),
            "passed_tests": sum(1 for r in self.results if r.passed),
        }
