# DSA Practice CLI - Complete Usage Guide

## 🚀 **Installation & Setup**

```bash
# Install the package in development mode
pip install -e .

# Verify installation
dsa --version
```

## 📋 **Available Commands**

### **1. Create New Solutions**
```bash
# Basic usage (LeetCode Easy by default)
dsa create 1 two-sum

# With specific platform and difficulty
dsa create --platform leetcode --difficulty medium 15 3sum
dsa create --platform codeforces --division div2 1000 problem-a
dsa create --platform topcoder --contest srm 800 algorithm-marathon
dsa create --platform codechef --type long 1000 optimization-problem

# Examples
dsa create 1 two-sum                    # LeetCode Easy
dsa create --difficulty hard 4 median-of-two-sorted-arrays
dsa create --platform codeforces --division div1 1000 problem-a
```

### **2. Run Solutions**
```bash
# Run with full analytics
dsa run 0001.two_sum
dsa run 0002.add_two_numbers
dsa run 0003.longest-substring

# Run with interactive mode
dsa run 0001.two_sum  # Includes interactive testing
```

### **3. Test Solutions**
```bash
# Run tests for specific solution
dsa test 0001.two_sum
dsa test 0002.add_two_numbers

# Run all tests
pytest
```

### **4. List & Search Solutions**
```bash
# List all solutions
dsa list

# Search by platform
dsa search --platform leetcode

# Search by difficulty
dsa search --platform leetcode --difficulty easy

# Search by multiple criteria
dsa search --platform codeforces --division div2
```

### **5. Edit Solutions**
```bash
# Open in default editor
dsa edit 0001.two_sum
dsa edit 0002.add_two_numbers

# Uses $EDITOR environment variable (defaults to 'code')
```

### **6. Maintenance Commands**
```bash
# Clean up generated files
dsa clean

# Install/update dependencies
dsa install
```

## 🎯 **Workflow Examples**

### **Complete Solution Creation Workflow**
```bash
# 1. Create a new solution
dsa create 5 longest-palindromic-substring --difficulty medium

# 2. Edit the solution
dsa edit 0005.longest-palindromic-substring

# 3. Add test cases to the TOML file
# Edit: data/test_cases/0005.longest-palindromic-substring.toml

# 4. Run the solution
dsa run 0005.longest-palindromic-substring

# 5. Test the solution
dsa test 0005.longest-palindromic-substring
```

### **Quick Development Workflow**
```bash
# Create solution
dsa create 6 zigzag-conversion --difficulty medium

# Edit and implement
dsa edit 0006.zigzag-conversion

# Test implementation
dsa run 0006.zigzag-conversion

# Run specific test cases
dsa run 0006.zigzag-conversion  # Use interactive mode: 'test 1', 'test 2', etc.
```

### **Platform-Specific Workflows**

#### **LeetCode Workflow**
```bash
# Easy problems
dsa create 1 two-sum
dsa create 9 palindrome-number

# Medium problems  
dsa create --difficulty medium 2 add-two-numbers
dsa create --difficulty medium 3 longest-substring-without-repeating-characters

# Hard problems
dsa create --difficulty hard 4 median-of-two-sorted-arrays
dsa create --difficulty hard 5 longest-palindromic-substring
```

#### **Codeforces Workflow**
```bash
# Division 2 problems
dsa create --platform codeforces --division div2 1000 problem-a
dsa create --platform codeforces --division div2 1000 problem-b

# Division 1 problems
dsa create --platform codeforces --division div1 1000 problem-a
dsa create --platform codeforces --division div1 1000 problem-b
```

#### **TopCoder Workflow**
```bash
# SRM problems
dsa create --platform topcoder --contest srm 800 algorithm-marathon
dsa create --platform topcoder --contest srm 800 dynamic-programming

# Marathon problems
dsa create --platform topcoder --contest marathon 100 optimization-problem
```

## 📁 **Generated File Structure**

When you run `dsa create`, it automatically generates:

```
solutions/leetcode/easy/0001.two_sum.py          # Solution file
data/test_cases/0001.two_sum.toml                # Test cases
```

### **Solution File Template**
```python
class TwoSum(BaseSolution):
    def solve(self, nums: List[int], target: int) -> List[int]:
        # Your algorithm here
        pass
    
    def solve_optimized(self, nums: List[int], target: int) -> List[int]:
        # Optional optimized version
        return self.solve(nums, target)
```

### **Test File Template**
```toml
[problem]
name = "Two Sum"
description = "Problem description goes here"
difficulty = "easy"
platform = "LeetCode"
problem_id = 1

[[test_cases]]
description = "Basic example"
input = [1, 2, 3]
expected = [0, 1]
timeout = 1.0
```

## 🔧 **Advanced Usage**

### **Custom Editor**
```bash
# Set custom editor
export EDITOR="vim"
dsa edit 0001.two_sum

# Or use VS Code
export EDITOR="code"
dsa edit 0001.two_sum
```

### **Batch Operations**
```bash
# Create multiple solutions
dsa create 1 two-sum
dsa create 2 add-two-numbers  
dsa create 3 longest-substring

# List all solutions
dsa list

# Run all solutions
for solution in $(dsa list --format=name); do
    dsa run $solution
done
```

### **Integration with Git**
```bash
# Create solution
dsa create 1 two-sum

# Edit and implement
dsa edit 0001.two_sum

# Test
dsa test 0001.two_sum

# Commit
git add solutions/leetcode/easy/0001.two_sum.py
git add data/test_cases/0001.two_sum.toml
git commit -m "Add Two Sum solution"
```

## 🎉 **Benefits**

### **1. Rapid Development**
- **One command** creates complete solution structure
- **Automatic file naming** with question numbers
- **Template customization** based on platform
- **Immediate testing** capabilities

### **2. Consistent Organization**
- **Standardized naming** across all platforms
- **Automatic directory structure** based on platform/difficulty
- **Consistent file formats** for solutions and tests

### **3. Developer Experience**
- **Rich CLI interface** with colors and formatting
- **Comprehensive help** and error messages
- **Search and filter** capabilities
- **Integration** with editors and tools

### **4. Scalability**
- **Supports all platforms** (LeetCode, Codeforces, TopCoder, CodeChef)
- **Handles any number** of problems
- **Easy to extend** with new platforms
- **Maintains organization** as collection grows

## 🚀 **Quick Start**

```bash
# 1. Install
pip install -e .

# 2. Create your first solution
dsa create 1 two-sum

# 3. Edit and implement
dsa edit 0001.two_sum

# 4. Run and test
dsa run 0001.two_sum

# 5. List all solutions
dsa list
```

The CLI tool makes DSA practice **fast, organized, and enjoyable**! 🎯
