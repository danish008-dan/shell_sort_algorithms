Shell Sort Algorithm - Python Implementation
============================================

Overview
--------
Shell Sort is an in-place comparison-based sorting algorithm.
It is an optimization over Insertion Sort that allows elements
to move across larger distances using a gap sequence.

Instead of comparing adjacent elements, Shell Sort compares
elements that are far apart, reducing the total number of shifts
required and improving efficiency for larger datasets.

How It Works
------------
1. The array is divided using a gap value.
2. Elements at the given gap are compared and sorted using
   insertion sort logic.
3. The gap is gradually reduced.
4. When the gap becomes 1, the algorithm behaves like insertion sort.
5. The array is fully sorted when the gap reaches 0.

Time Complexity
---------------
Best Case:    O(n log n)
Average Case: Depends on gap sequence
Worst Case:   O(n^2)

Space Complexity
----------------
O(1) - In-place sorting algorithm

Advantages
----------
- Faster than Insertion Sort for large arrays
- Simple and efficient
- Does not require extra memory

Disadvantages
-------------
- Worst-case time complexity is quadratic
- Performance depends on gap sequence

Use Cases
---------
- Medium-sized datasets
- When memory usage must be minimal
- As a foundational algorithm for understanding optimizations

Author
------
Your Name
