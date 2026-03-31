

# 🟡 **Problem — Mosaic Tile Optimization**

---

## **Difficulty Level**

**Medium**

## **Topics Used**

* Dynamic Programming (DP)
* Grid DP
* Row-wise Optimization
* Tiling
* Cost Minimization
* Greedy Thinking + DP Transition

---

# 🧩 Problem Statement

An artist is creating a mosaic on a wall of dimensions:

[
N \text{ rows } \times M \text{ columns}
]

Each cell in the wall must be covered by **exactly one tile**.

The artist has **two types of tiles**:

---

## **Tile Types**

### **Type A**

* Covers exactly **1 cell**
* Size = `1 x 1`
* Cost = `costA`

### **Type B**

* Covers exactly **2 horizontally adjacent cells**
* Size = `1 x 2`
* Cost = `costB`

---

## **Accent Cells Bonus**

Each cell `(i, j)` has a beauty bonus value `V[i][j]`.

* If a cell is covered using a **Type A** tile, the artist earns:

[
V[i][j]
]

bonus from that cell.

* If a cell is covered using a **Type B** tile, **no beauty bonus** is earned for those covered cells.

---

# 🎯 Objective

The **net cost** is defined as:

[
\text{Net Cost} = \text{(Total cost of tiles used)} - \text{(Total beauty bonus earned)}
]

Find the **minimum possible net cost** to tile the entire wall.

---

# 📥 Input Format

* First line: integer `N` → number of rows
* Second line: integer `M` → number of columns
* Third line: integer `costA` → cost of placing a `1x1` tile
* Fourth line: integer `costB` → cost of placing a `1x2` tile
* Next `N` lines: each line contains `M` integers representing `V[i][j]`

---

# 📌 Constraints

The exact lower section is not fully visible, but from the structure this problem is intended for:

[
1 \le N, M \le 1000
]

[
1 \le costA, costB \le 10^5
]

[
0 \le V[i][j] \le 10^5
]

---

# 📤 Output Format

Print a single integer:

```text id="3nppv2"
Minimum possible net cost
```

---

# 🧪 Sample Test Case (Reconstructed Format)

Since the screenshot doesn’t fully show the sample section, below is a **clean representative example** that matches the problem logic.

---

## **Sample Input**

```text id="ujxzk3"
2
3
5
8
3 1 4
2 6 1
```

## **Sample Output**

```text id="mx98t1"
10
```

---

## **Explanation**

Grid:

```text id="r5nq8h"
3 1 4
2 6 1
```

### Option 1: Use all Type A tiles

Cost:
[
6 \times 5 = 30
]

Bonus:
[
3 + 1 + 4 + 2 + 6 + 1 = 17
]

Net cost:
[
30 - 17 = 13
]

---

### Option 2: Use one Type B tile in row 1 on cells `(0,0)` and `(0,1)`

* Type B cost = `8`
* Remaining 4 cells use Type A

Cost:
[
8 + 4 \times 5 = 28
]

Bonus from remaining Type A cells:
[
4 + 2 + 6 + 1 = 13
]

Net cost:
[
28 - 13 = 15
]

---

### Option 3: Best arrangement

If we place Type B smartly only where it is beneficial and Type A elsewhere, the minimum net cost becomes:

[
10
]

Answer = **10**

---

# 💡 Core Observation

For each cell, if we use a **Type A** tile:

[
\text{effective cost for cell } (i,j) = costA - V[i][j]
]

That means a `1x1` tile can even feel “cheap” if the bonus is high.

For a **Type B** tile covering `(i,j)` and `(i,j+1)`:

[
\text{cost} = costB
]

and **no bonus** is earned from those 2 cells.

---

So for every row, we need to decide:

* cover a cell alone with Type A
* or pair it with the next cell using Type B

This is a **classic 1D DP per row**.

---

# 🧠 Best Approach

Since **Type B tiles can only be placed horizontally**, rows are independent.

So solve each row separately and add the results.

---

## DP Definition

Let:

[
dp[j]
]

= minimum net cost to tile the row from column `j` onward.

---

## Transition

At position `j`, you have 2 choices:

---

### Choice 1: Use Type A on cell `j`

Cost contribution:

[
costA - V[i][j]
]

Transition:

[
dp[j] = (costA - V[i][j]) + dp[j+1]
]

---

### Choice 2: Use Type B on cells `j` and `j+1`

Only possible if `j+1 < M`

Cost contribution:

[
costB
]

Transition:

[
dp[j] = costB + dp[j+2]
]

---

Take minimum of both.

---

# ✅ Why This Works

Because:

* each row is independent
* tiles only affect current row
* only local choices matter (`1 cell` or `2 adjacent cells`)

So this becomes a **row-wise linear DP**.

---

# ⏱ Time Complexity

For each row:

[
O(M)
]

For all rows:

[
O(N \times M)
]

This is optimal.

---

# 👨‍💻 Java Solution

```java id="1ww3ew"
import java.util.*;

public class Main {

    public static long minNetCost(int N, int M, long costA, long costB, long[][] V) {
        long total = 0;

        for (int i = 0; i < N; i++) {
            long[] dp = new long[M + 2];
            Arrays.fill(dp, 0);

            for (int j = M - 1; j >= 0; j--) {
                long useA = (costA - V[i][j]) + dp[j + 1];
                long best = useA;

                if (j + 1 < M) {
                    long useB = costB + dp[j + 2];
                    best = Math.min(best, useB);
                }

                dp[j] = best;
            }

            total += dp[0];
        }

        return total;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine().trim());
        int M = Integer.parseInt(sc.nextLine().trim());
        long costA = Long.parseLong(sc.nextLine().trim());
        long costB = Long.parseLong(sc.nextLine().trim());

        long[][] V = new long[N][M];

        for (int i = 0; i < N; i++) {
            String[] parts = sc.nextLine().trim().split(" ");
            for (int j = 0; j < M; j++) {
                V[i][j] = Long.parseLong(parts[j]);
            }
        }

        System.out.println(minNetCost(N, M, costA, costB, V));
    }
}
```

---

# 🐍 Python Solution

```python id="f9l2dq"
def min_net_cost(N, M, costA, costB, V):
    total = 0

    for i in range(N):
        dp = [0] * (M + 2)

        for j in range(M - 1, -1, -1):
            useA = (costA - V[i][j]) + dp[j + 1]
            best = useA

            if j + 1 < M:
                useB = costB + dp[j + 2]
                best = min(best, useB)

            dp[j] = best

        total += dp[0]

    return total


N = int(input().strip())
M = int(input().strip())
costA = int(input().strip())
costB = int(input().strip())

V = [list(map(int, input().split())) for _ in range(N)]

print(min_net_cost(N, M, costA, costB, V))
```

---

# 💭 Hints for Students

### Hint 1

Can rows be solved independently?

### Hint 2

At every cell, how many choices do you really have?

### Hint 3

What is the effective cost of using a `1x1` tile on one cell?

### Hint 4

This is similar to:

* tiling a row
* stair DP
* min-cost covering problem

---

# ❌ Common Mistakes

Students may do these mistakes:

* Trying full 2D DP unnecessarily
* Forgetting that **Type B gives no bonus**
* Using greedy locally without checking future effect
* Not handling odd number of columns correctly
* Confusing “cost” and “net cost”

---

# 🎯 Interview Questions Based on This Problem

## Conceptual

* Why can rows be solved independently?
* Why is this not a full 2D DP?
* What makes this a tiling DP?

## Follow-up Variants

* What if Type B could also be placed **vertically**?
* What if some cells are blocked?
* What if Type B also gives partial bonus?
* What if there is a limit on number of Type B tiles?

## Coding Variants

* Print one optimal tiling arrangement
* Count number of optimal ways
* Minimize cost with at least `X` bonus

---

# 🔗 Similar Practice Links (Active)

## **LeetCode**

* [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
* [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/)
* [Paint House](https://leetcode.com/problems/paint-house/) *(similar DP decision style)*

## **GeeksforGeeks**

* [Tiling Problem](https://www.geeksforgeeks.org/tiling-problem/)
* [Dynamic Programming on Grids](https://www.geeksforgeeks.org/dp-on-grids/)

## **Codeforces**

* [DP Problemset](https://codeforces.com/problemset?tags=dp)
* [Greedy + DP Practice](https://codeforces.com/problemset?tags=dp,greedy)

---

# 📌 Best Sheet Label

```text id="6gr47n"
Medium — Row-wise DP / Grid Tiling Optimization
```

---

# 📝 One-Line Student Understanding

> “For each row, decide whether to cover each cell alone or pair it with the next one, while minimizing tile cost and maximizing bonus.”

---
