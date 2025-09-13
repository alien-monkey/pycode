# Filename Convention Guide

## 📁 **Naming Convention**

All solution files and test cases now use a **4-digit zero-padded question number** as a prefix to ensure proper sorting.

### ✅ **Format**
```
0001.problem_name.py
0002.problem_name.py
0003.problem_name.py
...
```

### 📂 **File Structure**

#### **Solution Files**
```
solutions/
├── leetcode/
│   ├── easy/
│   │   ├── 0001.two_sum.py
│   │   ├── 0002.add_two_numbers.py
│   │   └── 0003.longest_substring.py
│   ├── medium/
│   │   ├── 0001.median_of_two_sorted_arrays.py
│   │   └── 0002.longest_palindromic_substring.py
│   └── hard/
│       ├── 0001.regular_expression_matching.py
│       └── 0002.merge_k_sorted_lists.py
├── codeforces/
│   ├── div1/
│   │   ├── 0001.problem_a.py
│   │   └── 0002.problem_b.py
│   └── div2/
│       ├── 0001.problem_a.py
│       └── 0002.problem_b.py
└── topcoder/
    ├── srm/
    │   ├── 0001.algorithm_marathon.py
    │   └── 0002.dynamic_programming.py
    └── marathon/
        ├── 0001.optimization_problem.py
        └── 0002.machine_learning.py
```

#### **Test Case Files**
```
data/test_cases/
├── 0001.two_sum.toml
├── 0002.add_two_numbers.toml
├── 0003.longest_substring.toml
└── 0004.median_of_two_sorted_arrays.toml
```

## 🎯 **Benefits**

### 1. **Automatic Sorting**
- Files are naturally sorted by question number
- Easy to find problems in order
- Consistent across all platforms

### 2. **Clear Organization**
- Question number is immediately visible
- Easy to reference specific problems
- Maintains chronological order

### 3. **Scalability**
- Works for any number of problems (0001-9999)
- Consistent naming across all platforms
- Easy to add new problems

## 📝 **Usage Examples**

### **Creating New Solutions**
```bash
# Copy template
cp solutions/leetcode/template.py solutions/leetcode/easy/0003.longest_substring.py

# Create test file
cp data/test_cases/template.toml data/test_cases/0003.longest_substring.toml

# Run solution
python solutions/leetcode/easy/0003.longest_substring.py
```

### **File References**
```python
# In solution files
if __name__ == "__main__":
    main_solution_runner(Solution, "data/test_cases/0003.longest_substring.toml")

# In test files
from solutions.leetcode.easy.longest_substring import LongestSubstring
```

## 🔢 **Number Assignment**

### **LeetCode**
- Use the official LeetCode problem number
- Example: LeetCode #1 → `0001.two_sum.py`
- Example: LeetCode #2 → `0002.add_two_numbers.py`

### **Codeforces**
- Use contest number or sequential numbering
- Example: Contest 1000, Problem A → `1000.problem_a.py`
- Example: Contest 1001, Problem B → `1001.problem_b.py`

### **TopCoder**
- Use SRM number or sequential numbering
- Example: SRM 800 → `0800.algorithm_name.py`
- Example: Marathon 100 → `0100.optimization_name.py`

## 📋 **Template Updates**

All templates now include the naming convention:

```python
"""
Usage:
    1. Copy this template to your problem file (use format: 0001.problem_name.py)
    2. Implement the solve() method
    3. Create a TOML test file in data/test_cases/ (use format: 0001.problem_name.toml)
    4. Run: python your_solution.py

Example:
    python solutions/leetcode/easy/0001.two_sum.py
"""
```

## ✅ **Current Files**

### **Renamed Files**
- `two_sum.py` → `0001.two_sum.py`
- `add_two_numbers.py` → `0002.add_two_numbers.py`
- `two_sum.toml` → `0001.two_sum.toml`
- `add_two_numbers.toml` → `0002.add_two_numbers.toml`

### **Updated References**
- All import statements updated
- All file paths updated
- All test files updated
- All templates updated

## 🎉 **Result**

The repository now has a **clean, organized structure** where:
- ✅ Files are automatically sorted by question number
- ✅ Easy to find and reference specific problems
- ✅ Consistent naming across all platforms
- ✅ Scalable for hundreds of problems
- ✅ Professional and maintainable structure
