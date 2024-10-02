### "Bulb Switcher" problem, also known as the "Benjamin Bulbs" problem

### Problem Statement

**Problem**: You have `n` bulbs initially turned off. You will toggle the state of the bulbs in `n` rounds according to the following rules:

1. In the first round, turn on all the bulbs.
2. In the second round, toggle every second bulb (turn it off if it’s on and vice versa).
3. In the third round, toggle every third bulb.
4. Continue this process until the `n`th round, where you only toggle the `n`th bulb.

Your task is to determine the number of bulbs that are on after `n` rounds.

### Input Format

- An integer `n` (0 ≤ n ≤ 10^9).

### Output Format

- Return an integer representing the number of bulbs that are on after `n` rounds.

### Example Input and Output

**Example 1**:
- **Input**: `n = 3`
- **Output**: `1`
- **Explanation**: The final state of the bulbs is [on, off, off], resulting in 1 bulb being on.

**Example 2**:
- **Input**: `n = 0`
- **Output**: `0`
- **Explanation**: No bulbs to toggle.

**Example 3**:
- **Input**: `n = 1`
- **Output**: `1`
- **Explanation**: The final state of the bulb is [on], resulting in 1 bulb being on.

### Constraints

- `0 <= n <= 10^9`

### Solution Explanation

The key insight is to realize that a bulb's final state depends on the number of times it is toggled. A bulb at position `k` is toggled once for each divisor it has. 

A bulb will remain ON if it is toggled an odd number of times, which only happens for perfect squares. For example, the number 36 has the divisors 1, 2, 3, 4, 6, 9, 12, 18, 36, but notice that pairs of divisors (like 1 and 36, 2 and 18) give us even counts, except for the square root (which is 6).

Thus, the bulbs that remain ON correspond to the perfect squares less than or equal to `n`. The count of such bulbs is equal to the largest integer `k` such that \( k^2 \leq n \), which is simply the integer part of the square root of `n`.

### Implementation

Here is how you can implement the solution in both **Java** and **Python**.

**Java Implementation**:
```java
public class BulbSwitcher {
    public static void main(String[] args) {
        int n = 3; // Example input
        System.out.println(countBulbs(n)); // Output: 1
    }

    public static int countBulbs(int n) {
        return (int) Math.sqrt(n);
    }
}
```

**Python Implementation**:
```python
import math

def count_bulbs(n):
    return int(math.sqrt(n))

# Example inputs
print(count_bulbs(3))  # Output: 1
print(count_bulbs(0))  # Output: 0
print(count_bulbs(1))  # Output: 1
```

### Explanation of the Code
- In both implementations, we calculate the integer square root of `n` using `Math.sqrt` in Java and `math.sqrt` in Python, then cast it to an integer.
- This effectively gives us the number of bulbs that remain ON after all the toggling operations. 

### Complexity Analysis
- **Time Complexity**: O(1) — The operations used to calculate the square root are constant time.
- **Space Complexity**: O(1) — We use a fixed amount of space regardless of the input size. 

### alternate solution 
```java
class Solution {
    public int bulbSwitch(int n) {
        int c=0;
        for(int i=1;i*i<=n;i++)
        {
// System.out.println(i*i);
           c++;
        }
        return c;
    }
}
```