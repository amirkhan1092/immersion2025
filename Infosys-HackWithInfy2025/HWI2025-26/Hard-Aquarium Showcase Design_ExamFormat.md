

# **Problem Title:** Aquarium Showcase Design

### **Difficulty Level:** Hard

### **Company Tag:** HWI (2026 Batch)

### **Topics Used:**

* Dynamic Programming
* 2D DP
* Sequence Merging
* State Transition
* Optimization

---

# **Problem Description**

An aquarium curator is designing a premium fish showcase by transferring fish from **two holding tanks** into a single long display.

You are given two tanks:

## **Tank A**

Contains `N` fish in a fixed order:

```text
A[1], A[2], ..., A[N]
```

## **Tank B**

Contains `M` fish in a fixed order:

```text
B[1], B[2], ..., B[M]
```

Each fish belongs to a family represented by an integer code from `1` to `K`.

---

## **Rules**

At each step, the curator may pick the **next fish from the front** of either:

* **Tank A**, or
* **Tank B**

Eventually, all fish are placed into one final row of length:

```text
N + M
```

### **Important**

The relative order of fish inside each tank must remain unchanged.

That means the final arrangement must be a valid **merge** of the two sequences.

---

# **Scoring**

For every adjacent pair of fish in the final display:

If a fish of family `x` is immediately followed by a fish of family `y`, then the score gained is:

```text
S[x][y]
```

The **total display score** is the sum of the scores of all adjacent pairs in the final merged row.

---

## **Task**

Find the **maximum possible total display score**.

---

# **Input Format**

* The first line contains an integer `N`, the number of fish in Tank A.
* The second line contains an integer `M`, the number of fish in Tank B.
* The third line contains an integer `K`, the number of distinct fish families.
* The next `K` lines each contain `K` space-separated integers, representing the score matrix `S`.
* The next `N` lines each contain an integer `A[i]`, the family of the `i-th` fish in Tank A.
* The next `M` lines each contain an integer `B[i]`, the family of the `i-th` fish in Tank B.

---

# **Output Format**

Print a single integer — the **maximum possible total display score**.

---

# **Constraints**

* `1 <= N <= 1000`
* `1 <= M <= 1000`
* `1 <= K <= 1000`
* `1 <= S[i][j] <= 10^5`
* `1 <= A[i], B[i] <= K`

---

# **Examples**

## **Example 1**

### **Input**

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

### **Output**

```text
7
```

### **Explanation**

Tank A:

```text
[2, 1]
```

Tank B:

```text
[2, 1, 2, 1]
```

One optimal merge is:

```text
2 2 1 1 2 1
```

Now compute adjacent pair scores:

* `S[2][2] = 2`
* `S[2][1] = 1`
* `S[1][1] = 2`
* `S[1][2] = 1`
* `S[2][1] = 1`

Total score:

```text
2 + 1 + 2 + 1 + 1 = 7
```

Hence, the answer is:

```text
7
```

---

## **Example 2**

### **Input**

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

### **Output**

```text
9
```

### **Explanation**

Tank A:

```text
[1, 2]
```

Tank B:

```text
[1, 1, 1, 1]
```

An optimal merge is:

```text
1 1 1 1 1 2
```

Adjacent pair scores:

* `S[1][1] = 2`
* `S[1][1] = 2`
* `S[1][1] = 2`
* `S[1][1] = 2`
* `S[1][2] = 1`

Total score:

```text
2 + 2 + 2 + 2 + 1 = 9
```

Hence, the answer is:

```text
9
```

---

# **Key Observation**

This is **not a greedy problem**.

The reason is:

* choosing the next fish affects not only the current score,
* but also the future possibilities,
* because the score depends on the **previous fish placed**.

So the state must remember:

* how many fish have already been taken from Tank A,
* how many fish have already been taken from Tank B,
* and **which tank the last fish came from**.

That naturally leads to **Dynamic Programming**.

---

# **Approach**

We build the final sequence step by step.

At any point:

* suppose we have taken `i` fish from Tank A
* and `j` fish from Tank B

Then the last fish placed in the merged row must be either:

* `A[i]` → if the last chosen fish came from Tank A
* `B[j]` → if the last chosen fish came from Tank B

So we define two DP states:

---

## **DP Definition**

### `dpA[i][j]`

Maximum score possible after taking:

* first `i` fish from Tank A
* first `j` fish from Tank B

such that the **last fish placed is `A[i]`**

---

### `dpB[i][j]`

Maximum score possible after taking:

* first `i` fish from Tank A
* first `j` fish from Tank B

such that the **last fish placed is `B[j]`**

---

# **Transitions**

## To compute `dpA[i][j]`

The last fish is `A[i]`.

That means just before it, the previous fish was either:

* `A[i-1]` (if we also picked from A previously), or
* `B[j]` (if the previous fish came from B)

So:

```text
dpA[i][j] = max(
    dpA[i-1][j] + S[A[i-1]][A[i]],
    dpB[i-1][j] + S[B[j]][A[i]]
)
```

(valid only where applicable)

---

## To compute `dpB[i][j]`

The last fish is `B[j]`.

So the previous fish was either:

* `B[j-1]`, or
* `A[i]`

Thus:

```text
dpB[i][j] = max(
    dpB[i][j-1] + S[B[j-1]][B[j]],
    dpA[i][j-1] + S[A[i]][B[j]]
)
```

(valid only where applicable)

---

# **Base Cases**

If only Tank A is used initially:

```text
dpA[i][0]
```

can be formed directly by placing fish from A in order.

Similarly, if only Tank B is used:

```text
dpB[0][j]
```

can be formed directly.

The first fish placed contributes **no score**, because score is only gained from **adjacent pairs**.

---

# **Java Solution (Exam Ready)**

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

        for (int i = 1; i <= N; i++) {
            A[i] = sc.nextInt();
        }

        for (int i = 1; i <= M; i++) {
            B[i] = sc.nextInt();
        }

        long[][] dpA = new long[N + 1][M + 1];
        long[][] dpB = new long[N + 1][M + 1];

        for (int i = 0; i <= N; i++) {
            Arrays.fill(dpA[i], NEG);
            Arrays.fill(dpB[i], NEG);
        }

        // Base case: first fish can come from A
        if (N >= 1) dpA[1][0] = 0;
        // Base case: first fish can come from B
        if (M >= 1) dpB[0][1] = 0;

        // Build only from A
        for (int i = 2; i <= N; i++) {
            dpA[i][0] = dpA[i - 1][0] + S[A[i - 1]][A[i]];
        }

        // Build only from B
        for (int j = 2; j <= M; j++) {
            dpB[0][j] = dpB[0][j - 1] + S[B[j - 1]][B[j]];
        }

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= M; j++) {

                // Transition to dpA[i][j]
                if (i > 0) {
                    // Previous also from A
                    if (i > 1 && dpA[i - 1][j] != NEG) {
                        dpA[i][j] = Math.max(dpA[i][j],
                                dpA[i - 1][j] + S[A[i - 1]][A[i]]);
                    }

                    // Previous from B
                    if (j > 0 && dpB[i - 1][j] != NEG) {
                        dpA[i][j] = Math.max(dpA[i][j],
                                dpB[i - 1][j] + S[B[j]][A[i]]);
                    }
                }

                // Transition to dpB[i][j]
                if (j > 0) {
                    // Previous also from B
                    if (j > 1 && dpB[i][j - 1] != NEG) {
                        dpB[i][j] = Math.max(dpB[i][j],
                                dpB[i][j - 1] + S[B[j - 1]][B[j]]);
                    }

                    // Previous from A
                    if (i > 0 && dpA[i][j - 1] != NEG) {
                        dpB[i][j] = Math.max(dpB[i][j],
                                dpA[i][j - 1] + S[A[i]][B[j]]);
                    }
                }
            }
        }

        long ans = Math.max(dpA[N][M], dpB[N][M]);
        System.out.println(ans);
    }
}
```

---

# **Why This Works**

At any stage of the merge:

* only the **last fish placed** matters for the next score contribution,
* because the score comes only from the next adjacent pair.

So the DP state only needs to track:

* how much of A is used,
* how much of B is used,
* and whether the last fish came from A or B.

This fully captures the problem.

Thus, the recurrence explores **all valid merges** while preserving relative order.

---

# **Time Complexity**

We compute DP over all `(i, j)` states.

There are:

```text
O(N * M)
```

states, and each state has constant transitions.

### **Overall Complexity**

```text
O(N * M)
```

With:

* `N <= 1000`
* `M <= 1000`

this is feasible.

---

# **Space Complexity**

We store two DP tables:

```text
O(N * M)
```

---

# **10 Hidden Test Cases**

These are useful for your **exam backend / hidden evaluator**.

---

## **Hidden Test Case 1**

### Input

```text
1
1
2
1 2
3 4
1
2
```

### Output

```text
2
```

### Explanation

Possible merges:

* `1 2` → score = `S[1][2] = 2`
* `2 1` → score = `S[2][1] = 3`

> Correct maximum is actually:

```text
3
```

### **Correct Output**

```text
3
```

---

## **Hidden Test Case 2**

### Input

```text
1
1
1
5
1
1
```

### Output

```text
5
```

---

## **Hidden Test Case 3**

### Input

```text
2
2
2
10 1
1 10
1
1
2
2
```

### Output

```text
21
```

### One optimal merge

```text
1 1 2 2
```

Score:

* `10 + 1 + 10 = 21`

---

## **Hidden Test Case 4**

### Input

```text
2
1
2
1 100
100 1
1
2
1
```

### Output

```text
200
```

### Optimal merge

```text
2 1 1
```

Score:

* `100 + 100 = 200`

---

## **Hidden Test Case 5**

### Input

```text
3
3
2
2 1
1 2
1
2
1
2
1
2
```

### Output

```text
9
```

---

## **Hidden Test Case 6**

### Input

```text
3
3
3
5 1 1
1 5 1
1 1 5
1
1
1
2
2
2
```

### Output

```text
22
```

### One optimal merge

```text
1 1 1 2 2 2
```

Score:

* `5 + 5 + 1 + 5 + 5 = 21`

> Correct checked total:

```text
21
```

### **Correct Output**

```text
21
```

---

## **Hidden Test Case 7**

### Input

```text
2
2
2
1 2
3 4
1
2
2
1
```

### Output

```text
9
```

---

## **Hidden Test Case 8**

### Input

```text
1
3
2
2 10
1 2
1
2
2
2
```

### Output

```text
14
```

### Optimal merge

```text
2 2 2 1
```

Score:

* `2 + 2 + 10 = 14`

---

## **Hidden Test Case 9**

### Input

```text
4
1
2
5 1
1 5
1
1
1
1
2
```

### Output

```text
16
```

### Merge

```text
1 1 1 1 2
```

Score:

* `5 + 5 + 5 + 1 = 16`

---

## **Hidden Test Case 10**

### Input

```text
2
2
2
100000 1
1 100000
1
2
1
2
```

### Output

```text
200001
```

### Optimal merge

```text
1 1 2 2
```

Score:

* `100000 + 1 + 100000 = 200001`

---

# **Important Exam Setter Notes**

## **1) Your original draft had one ambiguity**

You wrote:

> “Next K lines: S[i][j] matrix”

That should be explicitly stated as:

> The next `K` lines each contain `K` space-separated integers.

That is corrected above.

---

## **2) This is a true DP problem**

Students may incorrectly attempt:

* greedy merge,
* local best adjacency,
* choosing the larger immediate score.

Those approaches fail because the **future adjacency structure changes**.

So this is a very good **Hard screening / final round DP problem**.

---

## **3) Good educational framing**

This problem is very similar in spirit to:

* merging two strings,
* interleaving sequences,
* sequence DP with previous-state dependency.

So it is a strong “state-design” problem.

---

# **Recommended Interview / Viva Questions**

You can ask students:

1. Why does greedy fail here?
2. Why do we need to know **which tank the last fish came from**?
3. Can this be optimized in memory?
4. What if score depended on the **last two fish** instead of one?
5. Can you reconstruct the actual optimal merged sequence?

---


If you want that, send the next one and I’ll keep it in the same format.
