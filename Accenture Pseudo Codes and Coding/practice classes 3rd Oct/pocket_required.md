

### Problem Statement

**Problem**: Given an array of integers representing coins, determine the minimum number of pockets required to store all coins such that each pocket contains unique coins. 

### Input Format
- The first line contains an integer `N` (the number of coins).
- The second line contains `N` integers representing the values of the coins.

### Output Format
- Return an integer representing the minimum number of pockets required to store all coins without duplicates in each pocket.

### Example

**Input**:
```
8
1 2 2 3 4 4 4 5
```

**Output**:
```
5
```

### Explanation
In the provided example:
- We have coins with values: `[1, 2, 2, 3, 4, 4, 4, 5]`
- To store them in pockets:
  - Pocket 1: `1`
  - Pocket 2: `2`
  - Pocket 3: `3`
  - Pocket 4: `4`
  - Pocket 5: `5`
  
Each pocket contains unique values, and thus we need a total of 5 pockets to store all the coins.

### Approach to Solve the Problem

1. **Count the Frequency of Coins**: Use a set to identify unique coin values.
2. **Determine the Number of Pockets**: The size of this set will indicate the number of pockets required since each unique value can fit into its own pocket.

### Implementation

Here’s how you can implement this logic in Python:

```python
def min_pockets_required(n, coins):
    # Step 1: Use a set to store unique coins
    unique_coins = set(coins)
    
    # Step 2: The number of unique coins is equal to the number of pockets required
    return len(unique_coins)

# Example Input
n = 8
coins = [1, 2, 2, 3, 4, 4, 4, 5]

# Output the result
print(min_pockets_required(n, coins))  # Output: 5
```

### Complexity Analysis
- **Time Complexity**: O(N) where N is the number of coins, as we are iterating through the list to add values to the set.
- **Space Complexity**: O(U) where U is the number of unique coins stored in the set.

### Conclusion
This solution effectively determines the minimum number of pockets required to store the coins without duplicates. If you have further questions or would like additional details, feel free to ask!