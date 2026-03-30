
# 🔴 QUESTION 3 — HARD

# **Aquarium Showcase Design**

---

## 🧩 Problem Statement

An aquarium curator is designing a premium showcase by transferring fish from **two holding tanks** into a single long display.

---

## 🐟 Given

### Tank A

Contains `N` fish in a fixed order with family codes:

[
A[1], A[2], ..., A[N]
]

### Tank B

Contains `M` fish in a fixed order with family codes:

[
B[1], B[2], ..., B[M]
]

---

## 📜 Rules

At each step, the curator picks the **next fish from the front** of either:

* Tank A, or
* Tank B

Eventually all fish are placed into one final row of length `N + M`.

### Important:

The relative order inside each tank **must remain unchanged**.

---

## 🎯 Scoring

For every **adjacent pair** of fish in the final display:

If fish family = `x` followed by `y`, then score gained is:

[
S[x][y]
]

Total display score = sum of all adjacent pair scores.

---

## 🎯 Goal

Find the **maximum possible total display score**.

---

## 📥 Input Format

* First line: `N`
* Second line: `M`
* Third line: `K` → number of distinct families
* Next `K` lines: `S[i][j]` matrix
* Next `N` lines: fish families in Tank A
* Next `M` lines: fish families in Tank B

This full statement, constraints, and samples are visible in the Hard problem pages of your uploaded PDF 

---

## 📌 Constraints

* `1 <= N <= 1000`
* `1 <= M <= 1000`
* `1 <= K <= 1000`
* `1 <= S[i][j] <= 10^5`
* `1 <= A[i], B[i] <= K`

---

# 📤 Sample Input 1

```text
2
4
2
2 1
1 2
2
1
2
1
2
1
```

## 📤 Sample Output 1

```text
7
```

---

## ✅ Explanation

From the PDF explanation:

* `A = [2, 1]`
* `B = [2, 1, 2, 1]`

A good merge:

```text
2 2 1 1 2 1
```

Adjacent scores:

* `S[2][2] = 2`
* `S[2][1] = 1`
* `S[1][1] = 2`
* `S[1][2] = 1`
* `S[2][1] = 1`

Total = `7`

---

# 📤 Sample Input 2

```text
2
4
2
2 1
1 2
1
2
1
1
1
1
```

## 📤 Sample Output 2

```text
9
```

---

## ✅ Explanation

From the PDF explanation:

* `A = [1, 2]`
* `B = [1, 1, 1, 1]`

Best merge:

```text
1 1 1 1 1 2
```

Adjacent scores:

* `2 + 2 + 2 + 2 + 1 = 9`

---

# 🔍 Core Insight

This is an **interleaving + dynamic programming** problem.

We must merge two arrays while preserving order.

At every step, we choose:

* next from A
* or next from B

But score depends on the **last placed fish**.

So state must remember:

* how many used from A
* how many used from B
* what was the last fish source

---

# 🧠 DP Idea

Let:

* `dpA[i][j]` = max score after using first `i` fish from A and first `j` fish from B, **ending with A[i]**
* `dpB[i][j]` = same but **ending with B[j]**

---

# 🔁 Transition

## If last placed is `A[i]`

It could come from:

1. Previous also from A:
   [
   dpA[i-1][j] + S[A[i-1]][A[i]]
   ]

2. Previous from B:
   [
   dpB[i-1][j] + S[B[j]][A[i]]
   ]

Similarly for `dpB[i][j]`.

---

# ✅ Approach Summary

We fill DP table for all `(i, j)` combinations.

---

# ⏱️ Time Complexity

* Time: `O(N*M)`
* Space: `O(N*M)`

Given `N, M <= 1000`, this is acceptable.

---

# 💡 Hints for Students

### Hint 1

This is not greedy.

### Hint 2

The score depends on the **previous fish**, so last state matters.

### Hint 3

Think of merging two strings while maximizing adjacency score.

---

# 🎤 Interview Questions

* Why do we need 2 DP tables?
* Can we reduce memory?
* What if there were 3 tanks instead of 2?
* What if score depends on triplets instead of pairs?

---

# ✅ Java Solution

```java
import java.util.*;

public class Main {
    static final long NEG = Long.MIN_VALUE / 4;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();

        long[][] S = new long[K + 1][K + 1];
        for (int i = 1; i <= K; i++) {
            for (int j = 1; j <= K; j++) {
                S[i][j] = sc.nextLong();
            }
        }

        int[] A = new int[N + 1];
        int[] B = new int[M + 1];

        for (int i = 1; i <= N; i++) A[i] = sc.nextInt();
        for (int i = 1; i <= M; i++) B[i] = sc.nextInt();

        long[][] dpA = new long[N + 1][M + 1];
        long[][] dpB = new long[N + 1][M + 1];

        for (int i = 0; i <= N; i++) {
            Arrays.fill(dpA[i], NEG);
            Arrays.fill(dpB[i], NEG);
        }

        if (N >= 1) dpA[1][0] = 0;
        if (M >= 1) dpB[0][1] = 0;

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= M; j++) {

                if (i > 0 && dpA[i][j] > NEG) {
                    if (i + 1 <= N) {
                        dpA[i + 1][j] = Math.max(dpA[i + 1][j],
                                dpA[i][j] + S[A[i]][A[i + 1]]);
                    }
                    if (j + 1 <= M) {
                        dpB[i][j + 1] = Math.max(dpB[i][j + 1],
                                dpA[i][j] + S[A[i]][B[j + 1]]);
                    }
                }

                if (j > 0 && dpB[i][j] > NEG) {
                    if (i + 1 <= N) {
                        dpA[i + 1][j] = Math.max(dpA[i + 1][j],
                                dpB[i][j] + S[B[j]][A[i + 1]]);
                    }
                    if (j + 1 <= M) {
                        dpB[i][j + 1] = Math.max(dpB[i][j + 1],
                                dpB[i][j] + S[B[j]][B[j + 1]]);
                    }
                }
            }
        }

        System.out.println(Math.max(dpA[N][M], dpB[N][M]));
    }
}
```

---

# 🎓 FINAL LEARNING MAPPING FOR STUDENTS

| Question                 | Difficulty | Core Topic          | Subtopic               |
| ------------------------ | ---------- | ------------------- | ---------------------- |
| Coin Operations          | Easy       | Greedy + Math       | Modular Exponentiation |
| Coffee Shop Rewards      | Medium     | Dynamic Programming | Take/Skip DP           |
| Aquarium Showcase Design | Hard       | Dynamic Programming | 2D DP / Sequence Merge |

---



