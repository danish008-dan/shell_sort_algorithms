"""
File Name: shell_sort.py

Purpose:
--------
This file contains the implementation of the Shell Sort algorithm.
Shell Sort is an optimized version of Insertion Sort that allows
elements to move multiple positions at once using a gap strategy.
It improves performance on large datasets compared to simple
Insertion Sort.

Time Complexity:
----------------
Best Case:    O(n log n)
Average Case: Depends on gap sequence
Worst Case:   O(n^2)

Space Complexity:
-----------------
O(1) - In-place sorting algorithm
"""


def shell_sort(arr):
    # Get the length of the array
    n = len(arr)

    # Start with a big gap, then reduce the gap
    gap = n // 2

    # Continue until gap becomes 0
    while gap > 0:

        # Perform insertion sort for elements at gap distance
        for i in range(gap, n):
            # Store the current element
            temp = arr[i]

            # Initialize j for shifting elements
            j = i

            # Shift earlier gap-sorted elements until correct position is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Place temp at its correct position
            arr[j] = temp

        # Reduce the gap
        gap //= 2


# ------------------ Example Usage ------------------

# Unsorted array
data = [45, 23, 11, 89, 77, 98, 4, 28, 65]

print("Before Sorting:", data)

# Call shell sort function
shell_sort(data)

print("After Sorting:", data)
