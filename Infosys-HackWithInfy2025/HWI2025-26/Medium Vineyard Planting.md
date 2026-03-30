# Vineyard Planting

[check Solution](#solution)

### **Problem Description**

A vineyard manager is planting a new row of grapevines using seedlings from two nurseries:

- **Nursery A** has **N** seedlings with yield values $A[i]$.
- **Nursery B** has **M** seedlings with yield values $B[j]$.

The manager must plant all **N + M** seedlings in a single row. The seedlings from each nursery must appear in the row in their original relative order (e.g., if $A[0]$ is planted before $A[1]$ in the row, this constraint is satisfied; you cannot plant $A[1]$ before $A[0]$).

### **Scoring Rule**

The first seedling planted contributes **0** to the score. For every subsequent seedling with yield **x**, let:

- **max_prev** = maximum yield among all previously planted seedlings.
- **min_prev** = minimum yield among all previously planted seedlings.

The score contribution of **x** is:
$$\text{Score}(x) = \max(|x - \text{max\_prev}|, |x - \text{min\_prev}|)$$

Find the **maximum total score** achievable after planting all seedlings.

---

### **Input Format**

- The first line contains an integer, **N**, denoting the number of seedlings in nursery A.
- The next line contains an integer, **M**, denoting the number of seedlings in nursery B.
- Each line $i$ of the $N$ subsequent lines (where $0 \le i < N$) contains an integer describing $A[i]$.
- Each line $i$ of the $M$ subsequent lines (where $0 \le i < M$) contains an integer describing $B[i]$.

---

### **Constraints**

- $1 \le N \le 1000$
- $1 \le M \le 1000$
- $1 \le A[i] \le 10^5$
- $1 \le B[i] \le 10^5$

---

### **Sample Test Cases**

#### **Case 1**

**Input:**

```text
2
2
5
3
4
5

Output:
5

Explanation: We plant the seedling with yield 5 first to set the initial range. Next, we plant the seedling with yield 3, earning 2 points (distance to 5). Then we plant the seedling with yield 4, earning 1 point (distance to 3 or 5). Finally, we plant the remaining seedling with yield 5, earning 2 points (distance to 3). The total score is 5.
Case 2
Input:
2
1
10
20
100

Output:
170

Explanation: We start with the seedling of yield 10. We then immediately plant the high-value seedling with yield 100 to expand the range significantly, earning 90 points. This allows the remaining seedling with yield 20 to score 80 points (distance to 100), resulting in a total of 170.
Case 3
Input:
3
2
1
10
1
10
4

Output:
33

Explanation: We alternate to maximize distance from the extremes. The sequence starts with a yield of 1, then we plant a 10, earning 9 points. The next 1 earns another 9 points (distance to 10). The seedling with yield 4 earns 6 points (distance to 10), and finally, the last 1 earns 9 points (distance to 10). The total accumulated score is 33.
```

# solution

```java

import java.io.*;
import java.util.*;
import java.lang.Math;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        long[] a = new long[n];
        for(int i = 0; i < n; i++) {
            a[i] = sc.nextLong();
        }

        long[] b = new long[m];
        for(int i = 0; i < m; i++) {
            b[i] = sc.nextLong();
        }

        long[] minA = new long[n + 1];
        long[] maxA = new long[n + 1];
        minA[0] = Long.MAX_VALUE;
        maxA[0] = Long.MIN_VALUE;

        for(int i = 1; i <= n; i++) {
            minA[i] = Math.min(minA[i - 1], a[i - 1]);
            maxA[i] = Math.max(maxA[i - 1], a[i - 1]);
        }

        long[] minB = new long[m + 1];
        long[] maxB = new long[m + 1];
        minB[0] = Long.MAX_VALUE;
        maxB[0] = Long.MIN_VALUE;

        for(int i = 1; i <= m; i++) {
            minB[i] = Math.min(minB[i - 1], b[i - 1]);
            maxB[i] = Math.max(maxB[i - 1], b[i - 1]);
        }

        long[][] dp = new long[n + 1][m + 1];
        for(int i = 0; i <= n; i++) {
            for(int j = 0; j <= m; j++) {
                dp[i][j] = -1;
            }
        }

        for(int i = 0; i <= n; i++) {
            for(int j = 0; j <= m; j++) {
                if(i == 0 && j == 0) {
                    if(n > 0) {
                        dp[1][0] = Math.max(dp[1][0], 0);
                    }
                    if(m > 0) {
                        dp[0][1] = Math.max(dp[0][1], 0);
                    }
                    continue;
                }

                if(dp[i][j] == -1) {
                    continue;
                }

                long currMin = Math.min(minA[i], minB[j]);
                long currMax = Math.max(maxA[i], maxB[j]);

                if(i < n) {
                    long score = Math.max(Math.abs(a[i] - currMin), Math.abs(a[i] - currMax));
                    dp[i + 1][j] = Math.max(dp[i + 1][j], dp[i][j] + score);
                }
                if(j < m) {
                    long score = Math.max(Math.abs(b[j] - currMin), Math.abs(b[j] - currMax));
                    dp[i][j + 1] = Math.max(dp[i][j + 1], dp[i][j] + score);
                }
            }
        }
        System.out.println(dp[n][m]);
    }
}

```
