
# **Problem: Terrain Color Trail**

## **Problem Statement**

A hiker is traversing a rectangular terrain grid consisting of `N` rows and `M` columns.

The journey begins at the **top-left cell** `(0, 0)` and ends at the **bottom-right cell** `(N - 1, M - 1)`.

From any cell, the hiker is allowed to move **only**:

* **one step to the right**, or
* **one step downward**

The hiker’s **total score** is determined by **two components**:

---

## **1) Scenic Value**

Each cell `(i, j)` has a scenic value `V[i][j]`.

Whenever the hiker enters a cell, its scenic value is added to the total score.

> **Note:** The scenic value of the **starting cell** is also included.

---

## **2) Transition Bonus**

Each cell `(i, j)` also has a terrain **color code** `Color[i][j]`.

When the hiker moves from one cell to another:

* If the **color of the new cell** is the **same** as the color of the previous cell, the hiker earns an additional **bonus `B`**
* Otherwise, **no transition bonus** is awarded

---

## **Task**

Find the **maximum possible total score** the hiker can achieve by choosing an optimal path from the start cell to the destination.

---

# **Input Format**

* The first line contains an integer `N`, denoting the number of rows in the terrain grid.
* The second line contains an integer `M`, denoting the number of columns in the terrain grid.
* The third line contains an integer `B`, denoting the bonus awarded for moving to a cell of the **same color**.
* The next `N` lines each contain `M` space-separated integers representing the matrix `Color`.
* The next `N` lines each contain `M` space-separated integers representing the matrix `V`.

---

# **Output Format**

Print a single integer — the **maximum possible total score**.

---

# **Constraints**

* `1 <= N <= 1000`
* `1 <= M <= 1000`
* `1 <= B <= 1000`
* `1 <= Color[i][j] <= 1000`
* `1 <= V[i][j] <= 1000`

---

# **Sample Test Cases**

---

# **Example 1**

## **Input**

```text
2
2
10
1 1
2 1
5 5
5 5
```

## **Output**

```text
35
```

## **Explanation**

One optimal path is:

```text
(0,0) → (0,1) → (1,1)
```

### Scenic values collected:

* `(0,0) = 5`
* `(0,1) = 5`
* `(1,1) = 5`

Total scenic value:

```text
5 + 5 + 5 = 15
```

### Transition bonuses:

* `(0,0) → (0,1)` → same color (`1 → 1`) → `+10`
* `(0,1) → (1,1)` → same color (`1 → 1`) → `+10`

Total bonus:

```text
10 + 10 = 20
```

### Final score:

```text
15 + 20 = 35
```

---

# **Understanding the Problem**

At each step, the score contribution comes from:

## **If you move into cell `(i, j)`**

You gain:

[
V[i][j]
]

and possibly also:

[
+B
]

if:

[
Color[previous] = Color[i][j]
]

So each move depends only on:

* current cell value
* whether current color matches previous cell color

That means this is a **Dynamic Programming on Grid** problem.

---

# **Key Observation**

Since the hiker can only move:

* **right**
* **down**

every cell `(i, j)` can only be reached from:

* `(i-1, j)` → from above
* `(i, j-1)` → from left

So the best score at cell `(i, j)` depends only on the best score from those two previous cells.

---

# **DP State**

Let:

[
dp[i][j]
]

= maximum score obtainable upon reaching cell `(i, j)`.

---

# **Transition**

For each cell `(i, j)`:

## From top:

[
dp[i-1][j] + V[i][j] + \left( Color[i-1][j] == Color[i][j] ? B : 0 \right)
]

## From left:

[
dp[i][j-1] + V[i][j] + \left( Color[i][j-1] == Color[i][j] ? B : 0 \right)
]

So:

[
dp[i][j] = \max(\text{from top}, \text{from left})
]

---

# **Base Case**

Starting cell:

[
dp[0][0] = V[0][0]
]

because the hiker starts there and collects that value immediately.

---

# **Expected Complexity**

Since every cell is processed once:

* **Time Complexity:** `O(N × M)`
* **Space Complexity:** `O(N × M)`

This works well for:

[
N, M \le 1000
]

---

# **Java Solution (Clean Exam / Contest Style)**

```java
import java.util.*;

public class Solution {
    public static int solve(int N, int M, int B, int[][] color, int[][] value) {
        long[][] dp = new long[N][M];

        dp[0][0] = value[0][0];

        // First row
        for (int j = 1; j < M; j++) {
            dp[0][j] = dp[0][j - 1] + value[0][j];
            if (color[0][j] == color[0][j - 1]) {
                dp[0][j] += B;
            }
        }

        // First column
        for (int i = 1; i < N; i++) {
            dp[i][0] = dp[i - 1][0] + value[i][0];
            if (color[i][0] == color[i - 1][0]) {
                dp[i][0] += B;
            }
        }

        // Remaining cells
        for (int i = 1; i < N; i++) {
            for (int j = 1; j < M; j++) {
                long fromTop = dp[i - 1][j] + value[i][j];
                if (color[i - 1][j] == color[i][j]) {
                    fromTop += B;
                }

                long fromLeft = dp[i][j - 1] + value[i][j];
                if (color[i][j - 1] == color[i][j]) {
                    fromLeft += B;
                }

                dp[i][j] = Math.max(fromTop, fromLeft);
            }
        }

        return (int) dp[N - 1][M - 1];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int B = sc.nextInt();

        int[][] color = new int[N][M];
        int[][] value = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                color[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                value[i][j] = sc.nextInt();
            }
        }

        System.out.println(solve(N, M, B, color, value));
    }
}
```

---

# **Python Version (Student Friendly)**

```python
def solve(N, M, B, color, value):
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = value[0][0]

    # First row
    for j in range(1, M):
        dp[0][j] = dp[0][j - 1] + value[0][j]
        if color[0][j] == color[0][j - 1]:
            dp[0][j] += B

    # First column
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + value[i][0]
        if color[i][0] == color[i - 1][0]:
            dp[i][0] += B

    # Remaining cells
    for i in range(1, N):
        for j in range(1, M):
            from_top = dp[i - 1][j] + value[i][j]
            if color[i - 1][j] == color[i][j]:
                from_top += B

            from_left = dp[i][j - 1] + value[i][j]
            if color[i][j - 1] == color[i][j]:
                from_left += B

            dp[i][j] = max(from_top, from_left)

    return dp[N - 1][M - 1]


# Input
N = int(input())
M = int(input())
B = int(input())

color = [list(map(int, input().split())) for _ in range(N)]
value = [list(map(int, input().split())) for _ in range(N)]

print(solve(N, M, B, color, value))
```

---

# **Concepts Covered**

This problem is a good practice problem for:

* **2D Dynamic Programming**
* **Grid DP**
* **Path optimization**
* **State transition**
* **Maximum path sum variant**

---

# **Difficulty Level**

### Approximate Level:

* **LeetCode:** Medium
* **GeeksforGeeks:** Medium
* **Codeforces:** Div 2 A/B style DP

---

# **Similar Problems for Practice**

This problem is closest to:

## **LeetCode / GFG style topics**

* Maximum path sum in grid
* Minimum / maximum cost path
* DP on matrix
* Path with custom transition reward

### Search keywords:

```text
grid dp maximum path score
matrix dp right down movement
maximum score path in grid
dp with transition bonus
```

---

# **Suggested Better Title Options**

If you want to use this in your sheet, these titles are cleaner:

* **Terrain Color Trail**
* **Maximum Scenic Trail**
* **Colored Terrain Path**
* **Maximum Score Grid Path**
* **Grid Path with Color Bonus**

---

# **Teacher / Student Friendly Short Version**

If you want to paste this in a sheet, use this compact version:

---

## **Terrain Color Trail**

You are given:

* a grid `Color[N][M]`
* a grid `V[N][M]`
* an integer bonus `B`

You start at `(0,0)` and must reach `(N-1, M-1)`.

You may only move:

* right
* down

### Score Rules:

* Whenever you enter a cell, add its scenic value `V[i][j]`
* If you move to a cell having the **same color** as the previous cell, add bonus `B`

Find the **maximum total score** possible.

---

I
