"""
Timeout Detector Module
=======================

Provides timeout detection and "Time Limit Exceeded" simulation
for DSA solutions, mimicking LeetCode's timeout behavior.
"""

import signal
import time
from typing import Callable, Any, Optional
from contextlib import contextmanager


class TimeoutError(Exception):
    """Custom timeout exception"""

    pass


class TimeoutDetector:
    """Detects and handles timeouts in solution execution"""

    def __init__(self, timeout_seconds: float = 1.0):
        self.timeout_seconds = timeout_seconds
        self.original_handler = None

    def timeout_handler(self, signum, frame):
        """Signal handler for timeout"""
        raise TimeoutError(f"Time limit exceeded: {self.timeout_seconds}s")

    @contextmanager
    def timeout_context(self):
        """Context manager for timeout detection"""
        # Set up signal handler
        self.original_handler = signal.signal(signal.SIGALRM, self.timeout_handler)
        signal.alarm(int(self.timeout_seconds))

        try:
            yield
        finally:
            # Restore original handler
            signal.alarm(0)
            if self.original_handler:
                signal.signal(signal.SIGALRM, self.original_handler)

    def run_with_timeout(self, func: Callable, *args, **kwargs) -> Any:
        """Run function with timeout detection"""
        try:
            with self.timeout_context():
                return func(*args, **kwargs)
        except TimeoutError as e:
            print(f"⏰ {e}")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

    def simulate_leetcode_timeout(
        self, solution: Any, test_cases: list, time_limit: float = 1.0
    ) -> dict:
        """Simulate LeetCode's timeout behavior"""
        results = {
            "passed": 0,
            "failed": 0,
            "timeout": 0,
            "total_time": 0,
            "timeout_cases": [],
        }

        self.timeout_seconds = time_limit

        for i, test_case in enumerate(test_cases):
            start_time = time.time()

            try:
                with self.timeout_context():
                    if hasattr(test_case, "input"):
                        if isinstance(test_case.input, (list, tuple)):
                            result = solution.solve(*test_case.input)
                        else:
                            result = solution.solve(test_case.input)
                    else:
                        result = solution.solve()

                    execution_time = time.time() - start_time
                    results["total_time"] += execution_time

                    # Check if solution is correct
                    expected = getattr(test_case, "expected", None)
                    if expected is None or result == expected:
                        results["passed"] += 1
                        print(f"✅ Test {i+1}: PASSED ({execution_time:.3f}s)")
                    else:
                        results["failed"] += 1
                        print(
                            f"❌ Test {i+1}: FAILED - Expected: {expected}, Got: {result}"
                        )

            except TimeoutError:
                results["timeout"] += 1
                results["timeout_cases"].append(i + 1)
                print(f"⏰ Test {i+1}: TIME LIMIT EXCEEDED")

            except Exception as e:
                results["failed"] += 1
                print(f"❌ Test {i+1}: ERROR - {e}")

        return results


def detect_timeout_issues(
    solution: Any, test_cases: list, time_limits: list = [0.1, 0.5, 1.0, 2.0]
) -> dict:
    """Detect timeout issues across different time limits"""
    detector = TimeoutDetector()
    results = {}

    print("🔍 Analyzing timeout behavior...")
    print("=" * 50)

    for time_limit in time_limits:
        print(f"\nTesting with {time_limit}s time limit:")
        result = detector.simulate_leetcode_timeout(solution, test_cases, time_limit)
        results[time_limit] = result

        print(f"  Passed: {result['passed']}")
        print(f"  Failed: {result['failed']}")
        print(f"  Timeout: {result['timeout']}")
        print(f"  Total time: {result['total_time']:.3f}s")

    return results


if __name__ == "__main__":
    # Example usage
    class ExampleSolution:
        def solve(self, nums):
            # Simulate a slow solution
            time.sleep(0.2)
            return sum(nums)

    solution = ExampleSolution()
    test_cases = [
        type("TestCase", (), {"input": [1, 2, 3], "expected": 6})(),
        type("TestCase", (), {"input": [4, 5, 6], "expected": 15})(),
    ]

    detect_timeout_issues(solution, test_cases)
