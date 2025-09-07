# Data-Analysis-Projects-
Various Data Analysis Projects 
# Mean-Variance-Standard Deviation Calculator 📊

A Python project that calculates statistical measures (mean, variance, standard deviation, max, min, and sum) for a 3×3 matrix using NumPy.

## 🎯 Overview

This calculator takes a list of 9 numbers, converts it into a 3×3 NumPy array, and computes various statistical measures along different axes:
- **Axis 0**: Statistics calculated down each column (3 values)
- **Axis 1**: Statistics calculated across each row (3 values)
- **Flattened**: Statistics for the entire matrix as a 1D array (1 value)

## 📋 Features

- ✅ Input validation (ensures exactly 9 numbers)
- ✅ Comprehensive statistical calculations
- ✅ Clean dictionary output format
- ✅ Error handling with descriptive messages
- ✅ Random matrix testing

## 🏗️ Project Structure

```
📁 Project Directory
├── 📄 mean_var_std.py    # Core calculation function
├── 📄 main.py           # Test script with random matrix
└── 📄 README.md         # This documentation
```

## 🔧 Requirements

- Python 3.x
- NumPy

Install NumPy if you haven't already:
```bash
pip install numpy
```

## 🚀 Usage

### Basic Usage

```python
from mean_var_std import calculate

# Example with sequential numbers
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
```

### Running the Test

```bash
python3 main.py
```

This will generate a random 3×3 matrix and display all calculated statistics.

## 📊 Function Details

### `calculate(list)`

**Parameters:**
- `list`: A list containing exactly 9 numbers

**Returns:**
A dictionary with the following structure:
```python
{
  'mean': [axis0_values, axis1_values, flattened_value],
  'variance': [axis0_values, axis1_values, flattened_value],
  'standard deviation': [axis0_values, axis1_values, flattened_value],
  'max': [axis0_values, axis1_values, flattened_value],
  'min': [axis0_values, axis1_values, flattened_value],
  'sum': [axis0_values, axis1_values, flattened_value]
}
```

**Raises:**
- `ValueError`: If the input list doesn't contain exactly 9 elements

## 📝 Example

### Input:
```python
calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

### Matrix Representation:
```
[[0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]]
```

### Output:
```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## 🧮 Understanding the Axes

- **Axis 0 (Columns)**: Calculates statistics vertically down each column
  - Column 1: [0, 3, 6] → mean = 3.0
  - Column 2: [1, 4, 7] → mean = 4.0  
  - Column 3: [2, 5, 8] → mean = 5.0

- **Axis 1 (Rows)**: Calculates statistics horizontally across each row
  - Row 1: [0, 1, 2] → mean = 1.0
  - Row 2: [3, 4, 5] → mean = 4.0
  - Row 3: [6, 7, 8] → mean = 7.0

- **Flattened**: Treats the entire matrix as [0, 1, 2, 3, 4, 5, 6, 7, 8] → mean = 4.0

## ⚠️ Error Handling

The function will raise a `ValueError` with the message "List must contain nine numbers." if:
- The input list has fewer than 9 elements
- The input list has more than 9 elements

## 🧪 Testing

Run the included test script to see the function in action with a randomly generated matrix:

```bash
python3 main.py
```

Each run will generate a new random 3×3 matrix using digits 0-9, perfect for testing the statistical calculations.

## 📚 Dependencies

- **NumPy**: Used for efficient array operations and statistical calculations
- **Random**: Used in the test script for generating random matrices

---

*This project demonstrates practical use of NumPy for statistical calculations and matrix operations.*
