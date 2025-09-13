#!/usr/bin/env python3
"""
Simple test runner for Two Sum solution with analytics
"""

import sys
import os
import time
import traceback
from typing import List, Any

# Add the project root to the path
sys.path.insert(0, os.path.dirname(__file__))

from src.platforms.leetcode.easy.0001.two_sum import TwoSum
from utils.testing.test_runner import TestRunner
from utils.benchmarking.performance_analyzer import PerformanceAnalyzer


def run_performance_benchmark():
    """Run performance benchmark tests"""
    print("🚀 Running Performance Benchmark Tests")
    print("=" * 60)
    
    solution = TwoSum()
    
    # Test cases
    test_cases = [
        {"input": ([2, 7, 11, 15], 9), "expected": [0, 1], "description": "Basic example"},
        {"input": ([3, 2, 4], 6), "expected": [1, 2], "description": "Different indices"},
        {"input": ([3, 3], 6), "expected": [0, 1], "description": "Same numbers"},
        {"input": ([1, 2, 3, 4, 5], 9), "expected": [3, 4], "description": "Larger array"},
        {"input": ([1, 2, 3, 4, 5], 10), "expected": [], "description": "No solution"},
    ]
    
    # Test brute force solution
    print("\n📊 Testing Brute Force Solution (O(n²))")
    print("-" * 40)
    
    brute_force_times = []
    for i, test_case in enumerate(test_cases):
        nums, target = test_case["input"]
        expected = test_case["expected"]
        description = test_case["description"]
        
        start_time = time.time()
        result = solution.solve(nums, target)
        end_time = time.time()
        
        execution_time = end_time - start_time
        brute_force_times.append(execution_time)
        
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i+1}: {description}")
        print(f"  Input: nums={nums}, target={target}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Time: {execution_time:.6f}s")
        print(f"  Status: {status}")
        print()
    
    # Test optimized solution
    print("\n📊 Testing Optimized Solution (O(n))")
    print("-" * 40)
    
    optimized_times = []
    for i, test_case in enumerate(test_cases):
        nums, target = test_case["input"]
        expected = test_case["expected"]
        description = test_case["description"]
        
        start_time = time.time()
        result = solution.solve_optimized(nums, target)
        end_time = time.time()
        
        execution_time = end_time - start_time
        optimized_times.append(execution_time)
        
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i+1}: {description}")
        print(f"  Input: nums={nums}, target={target}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Time: {execution_time:.6f}s")
        print(f"  Status: {status}")
        print()
    
    # Performance comparison
    print("\n📈 Performance Comparison")
    print("-" * 40)
    
    avg_brute_force = sum(brute_force_times) / len(brute_force_times)
    avg_optimized = sum(optimized_times) / len(optimized_times)
    
    print(f"Average Brute Force Time: {avg_brute_force:.6f}s")
    print(f"Average Optimized Time: {avg_optimized:.6f}s")
    
    if avg_brute_force > 0:
        speedup = avg_brute_force / avg_optimized if avg_optimized > 0 else float('inf')
        print(f"Speedup: {speedup:.2f}x")
    
    print("\n🎯 Performance Analysis")
    print("-" * 40)
    
    # Analyze time complexity
    print("Time Complexity Analysis:")
    print("  Brute Force: O(n²) - Nested loops")
    print("  Optimized: O(n) - Single pass with hash map")
    
    print("\nSpace Complexity Analysis:")
    print("  Brute Force: O(1) - No extra space")
    print("  Optimized: O(n) - Hash map storage")
    
    print("\n✅ Performance benchmark completed!")


def run_comprehensive_tests():
    """Run comprehensive test suite"""
    print("🧪 Running Comprehensive Test Suite")
    print("=" * 60)
    
    try:
        # Run pytest
        import subprocess
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/unit/test_two_sum.py", 
            "-v", "--tb=short"
        ], capture_output=True, text=True)
        
        print("Pytest Output:")
        print(result.stdout)
        
        if result.stderr:
            print("Pytest Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ All tests passed!")
        else:
            print("❌ Some tests failed!")
            
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        traceback.print_exc()


def run_analytics():
    """Run analytics and performance analysis"""
    print("📊 Running Analytics")
    print("=" * 60)
    
    try:
        solution = TwoSum()
        
        # Test with different input sizes
        input_sizes = [10, 100, 1000, 5000]
        times_brute = []
        times_optimized = []
        
        for size in input_sizes:
            # Create test data
            nums = list(range(size))
            target = size * 2 - 1  # Last two elements
            
            # Test brute force
            start = time.time()
            result1 = solution.solve(nums, target)
            time1 = time.time() - start
            times_brute.append(time1)
            
            # Test optimized
            start = time.time()
            result2 = solution.solve_optimized(nums, target)
            time2 = time.time() - start
            times_optimized.append(time2)
            
            print(f"Size {size}: Brute={time1:.6f}s, Optimized={time2:.6f}s")
        
        # Analyze growth
        print("\n📈 Growth Analysis:")
        for i in range(1, len(input_sizes)):
            size_ratio = input_sizes[i] / input_sizes[i-1]
            time_ratio_brute = times_brute[i] / times_brute[i-1] if times_brute[i-1] > 0 else 1
            time_ratio_opt = times_optimized[i] / times_optimized[i-1] if times_optimized[i-1] > 0 else 1
            
            print(f"Size increase: {size_ratio:.1f}x")
            print(f"  Brute force time increase: {time_ratio_brute:.1f}x")
            print(f"  Optimized time increase: {time_ratio_opt:.1f}x")
        
    except Exception as e:
        print(f"❌ Error running analytics: {e}")
        traceback.print_exc()


def main():
    """Main test runner"""
    print("🎯 DSA Practice - Two Sum Solution Test Runner")
    print("=" * 60)
    
    try:
        # Run performance benchmark
        run_performance_benchmark()
        
        print("\n" + "=" * 60)
        
        # Run comprehensive tests
        run_comprehensive_tests()
        
        print("\n" + "=" * 60)
        
        # Run analytics
        run_analytics()
        
        print("\n🎉 All tests completed!")
        
    except Exception as e:
        print(f"❌ Error in main: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()