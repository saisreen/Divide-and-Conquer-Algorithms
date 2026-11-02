# Divide-and-Conquer Algorithms: Merge Sort and Quick Sort

## Project Overview

This project is part of Assignment 2: Analyzing and Implementing Divide-and-Conquer Algorithms.

The main purpose of this project is to understand how Merge Sort and Quick Sort work and compare their performance using Python.

Both algorithms follow the divide-and-conquer approach, where a large problem is divided into smaller problems to make it easier to solve.

## Algorithms Implemented

### 1. Merge Sort

Merge Sort divides the input array into two halves, sorts each half recursively, and combines the sorted elements.

- Best-case time complexity: O(n log n)
- Average-case time complexity: O(n log n)
- Worst-case time complexity: O(n log n)
- Additional space complexity: O(n)

### 2. Quick Sort

Quick Sort selects a pivot element and arranges the remaining elements around it. It then sorts the partitions recursively.

This implementation uses the last element as the pivot and performs in-place partitioning.

- Best-case time complexity: O(n log n)
- Average-case time complexity: O(n log n)
- Worst-case time complexity: O(n²)
- Additional space complexity: O(log n) for the implemented stack-optimized version

## Technologies Used

- Python 3
- `time` module for execution-time measurement
- `tracemalloc` module for memory measurement
- `random` module for generating test data
- `csv` module for saving performance results

## Project Files

```text
Divide-and-Conquer-Algorithms/
│
├── divide_conquer_benchmark.py
├── sorting_results.csv
└── README.md
```

**divide_conquer_benchmark.py**

Contains the implementation of Merge Sort and Quick Sort, along with performance testing.

**sorting_results.csv**

Contains execution-time and peak memory measurements for different input sizes and dataset types.

**README.md**

Contains the project description and instructions for running the program.

## Datasets Used

Both algorithms are tested using three types of datasets:

1. Sorted data: Elements arranged in ascending order.
2. Reverse-sorted data: Elements arranged in descending order.
3. Random data: Elements arranged in random order.

The input sizes used are 100, 500, and 1,000 elements.

## How to Run the Project

Step 1: Install Python 3.

Step 2: Download or clone this GitHub repository.

Step 3: Open the project folder in a terminal.

Step 4: Run the following command:

```bash
python divide_conquer_benchmark.py
```

Step 5: The program executes both sorting algorithms and records their performance.

Step 6: Open `sorting_results.csv` to review the execution time and memory usage.

No external Python packages are required.

## Performance Comparison

The performance comparison focuses on:

- Execution time in milliseconds
- Peak additional Python memory allocations
- Different input sizes
- Sorted, reverse-sorted, and random datasets

Merge Sort generally provides consistent performance because it divides the input into equal halves.

Quick Sort can perform efficiently on random datasets. However, selecting the last element as the pivot can cause slower performance for sorted and reverse-sorted inputs.

The actual results depend on the input data, Python execution environment, and computer performance.

## Conclusion

This project helped me understand how divide-and-conquer algorithms work in practice.

Merge Sort provides predictable sorting performance but requires additional memory. Quick Sort can use less additional memory, but its execution time depends on pivot selection.

By implementing and testing both algorithms, I was able to compare theoretical time complexity with practical performance.

## Author

Sai Sree

Assignment : Analyzing and Implementing Divide-and-Conquer Algorithms
