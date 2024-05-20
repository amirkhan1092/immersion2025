If you are not talking about finding the \(k\)-th smallest element but instead about merging two sorted arrays to find the \(k\)-th element in the merged array, here’s an efficient solution:

### Problem:
Given two sorted arrays \(A\) and \(B\) of lengths \(m\) and \(n\) respectively, find the \(k\)-th element in the merged array of \(A\) and \(B\) without explicitly merging the arrays.

### Solution:
The solution uses a binary search approach similar to finding the median of two sorted arrays, but adjusted for finding the \(k\)-th element.

### Steps:

1. **Ensure \(A\) is the smaller array:**
   If \(m > n\), swap \(A\) and \(B\) to make sure \(A\) is the smaller array.

2. **Binary search setup:**
   Perform binary search on array \(A\). Initialize \( \text{low} = \max(0, k - n) \) and \( \text{high} = \min(k, m) \).

3. **Binary search:**
   - Set \( \text{low} = \max(0, k - n) \) and \( \text{high} = \min(k, m) \).
   - Perform the binary search:
     - Calculate \( i = \frac{\text{low} + \text{high}}{2} \) (partition index for \(A\)).
     - Calculate \( j = k - i \) (partition index for \(B\)).
     
4. **Check and adjust partitions:**
   - If \( i < m \) and \( j > 0 \) and \( B[j-1] > A[i] \), increase \( \text{low} \) to \( i + 1 \).
   - If \( i > 0 \) and \( j < n \) and \( A[i-1] > B[j] \), decrease \( \text{high} \) to \( i - 1 \).
   - Otherwise, you have found the correct partition.

5. **Determine the \(k\)-th element:**
   - If the partition is valid, the \(k\)-th element will be the maximum of the left partition:
     - If \( i = 0 \), the \(k\)-th element is \( B[j-1] \).
     - If \( j = 0 \), the \(k\)-th element is \( A[i-1] \).
     - Otherwise, it is \( \max(A[i-1], B[j-1]) \).

### Pseudocode:
Here's the pseudocode to implement the binary search approach:

```python
def findKthElement(A, B, k):
    m, n = len(A), len(B)
    
    # Ensure A is the smaller array
    if m > n:
        return findKthElement(B, A, k)
    
    low, high = max(0, k - n), min(k, m)
    
    while low <= high:
        i = (low + high) // 2
        j = k - i
        
        if i < m and j > 0 and B[j-1] > A[i]:
            low = i + 1
        elif i > 0 and j < n and A[i-1] > B[j]:
            high = i - 1
        else:
            if i == 0:
                return B[j-1]
            if j == 0:
                return A[i-1]
            return max(A[i-1], B[j-1])
    
    return -1  # If no valid partition is found (shouldn't happen with valid input)
```

### Example:
Consider arrays:
\[ A = [2, 3, 6, 7, 9] \]
\[ B = [1, 4, 8, 10] \]
and you want to find the 5th element in the merged array.

- Ensure \(A\) is the smaller array (which it is).
- Perform binary search with \( k = 5 \).
- Calculate partitions and find the 5th element without merging the arrays.

By following this approach, you can efficiently find the \(k\)-th element in the merged array with a time complexity of \(O(\log \min(m, n))\).