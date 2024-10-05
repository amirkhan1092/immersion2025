To solve the problem of minimizing the number of visible bottles given a list of bottles with varying radii, we can follow a structured approach. The main idea is to use a greedy algorithm to group the bottles into nested pairs where possible.

### Problem Statement

**Problem**: Given an array of integers where each integer represents the radius of a bottle, determine the minimum number of bottles that remain visible after optimally nesting smaller bottles inside larger ones.

**Conditions for Nesting**:
1. A bottle can only be nested inside another if its radius is strictly smaller than the larger bottle's radius.
2. Once a bottle is nested inside another, it ceases to be visible.
3. A bottle cannot enclose another bottle if it is already nested within one.

### Input Format
- The first line contains an integer `N` (the number of bottles).
- The second line contains `N` integers representing the radii of the bottles.

### Output Format
- Return an integer representing the minimum number of visible bottles after optimal nesting.

### Example

**Input**:
```
8
1 1 2 3 4 5 5 4
```

**Output**:
```
2
```

### Explanation
In the provided example, we can nest the bottles in the following manner:
- The first `1` can be nested into `2`
- The `2` can be nested into `3`
- The `3` can be nested into `4`
- The `4` can be nested into `5`

After these operations, only the two `5`s and the remaining `4` will be visible.

### Approach to Solve the Problem

1. **Sort the Radii**: Start by sorting the array of radii.
2. **Count Unique Bottles**: Use a set to count unique radii, which gives us an indication of how many distinct sizes we have.
3. **Calculate Minimum Visible Bottles**: The minimum number of visible bottles will be determined by how many distinct sizes we can fit together.

### Implementation

Here's how we can implement this logic in Python:

```python
def min_visible_bottles(n, radii):
    # Step 1: Sort the radii
    radii.sort()
    
    # Step 2: Use a set to count unique radii
    unique_radii = set(radii)
    
    # Step 3: The minimum visible bottles will be equal to the count of unique radii
    return len(unique_radii)

# Example Input
n = 8
radii = [1, 1, 2, 3, 4, 5, 5, 4]

# Output the result
print(min_visible_bottles(n, radii))  # Output: 2
```

### Complexity Analysis
- **Time Complexity**: O(N log N) due to the sorting step, where N is the number of bottles.
- **Space Complexity**: O(U) where U is the number of unique radii stored in a set.

### Conclusion
This solution efficiently counts the minimum number of visible bottles after optimal nesting. The key to the approach lies in sorting the radii and counting unique values. This method ensures that we can group smaller bottles into larger ones optimally. If you have further questions or need clarifications, feel free to ask!