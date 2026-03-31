

# 🔴 **Problem — Spice Blend Sequencing**

---

## **Difficulty Level**

**Hard**

## **Topics Used**

* Dynamic Programming
* Sequence Merging
* State DP
* Prefix Selection
* Ordered Interleaving
* Optimization DP

---

# 🧩 Problem Statement

A chef is creating a signature spice blend by combining spices from **2 different regional collections**.

* **Collection A** has `N` spices.
* **Collection B** has `M` spices.

The chef must select **exactly `K` spices** in total to create the blend.

At each step, the chef picks the **next available spice from the front** of either Collection **A** or Collection **B**.

### Important Rules:

* The **relative order** of spices within each collection **must be preserved**.
* Each spice has:

  * a **flavor profile** (an integer category)
  * an **intensity value**

---

## **Scoring Rules**

### 1) Intensity Score

The intensity of every selected spice is **added** to the total score.

### 2) Harmony Bonus

Whenever **two consecutive selected spices** in the final blend have the **same flavor profile**, an additional:

[
H
]

points are added.

---

## **Goal**

Find the **maximum total score** achievable by selecting **exactly `K` spices**.

[
\text{Total Score} = \text{Sum of Intensities} + \text{Harmony Bonuses}
]

---

# 📥 Input Format

* The first line contains an integer `N`, denoting the number of spices in collection **A**.
* The second line contains an integer `M`, denoting the number of spices in collection **B**.
* The third line contains an integer `K`, denoting the total number of spices to select.
* The fourth line contains an integer `H`, denoting the harmony bonus value.

### Next `N` lines:

Each line contains **2 space-separated integers**:

```text id="4wzvfh"
flavor intensity
```

describing a spice in collection **A**.

### Next `M` lines:

Each line contains **2 space-separated integers**:

```text id="h3n9pv"
flavor intensity
```

describing a spice in collection **B**.

---

# 📌 Constraints

[
1 \le N \le 1000
]

[
1 \le M \le 1000
]

[
1 \le K \le N + M
]

[
1 \le H \le 10^5
]

[
1 \le A[i][j] \le 10^5
]

[
1 \le B[i][j] \le 10^5
]

---

# 📤 Output Format

Print a single integer — the **maximum total score**.

---

# 🧪 Sample Test Cases

---

## **Case 1**

### Input

```text id="wpe48h"
2
1
3
50
1 10
2 20
1 15
```

### Output

```text id="kgmhz2"
95
```

### Explanation

We must select exactly **3 spices**, so all spices are selected.

A good sequence is:

```text id="xjvl74"
B1 -> A1 -> A2
```

Which corresponds to flavors:

```text id="2te4eg"
1 -> 1 -> 2
```

### Score:

* Intensity sum:

[
15 + 10 + 20 = 45
]

* Harmony bonus:

  * `B1` and `A1` have same flavor `1` → `+50`

### Total:

[
45 + 50 = 95
]

---

## **Case 2**

### Input

```text id="62h4rj"
2
2
3
10
1 10
2 10
2 10
1 10
```

### Output

```text id="r5wzls"
40
```

### Explanation

We must choose exactly **3 spices**.

One optimal selection/order is:

```text id="1l4vhh"
A1 -> A2 -> B1
```

Flavors:

```text id="jjwdxg"
1 -> 2 -> 2
```

### Score:

* Intensity sum:

[
10 + 10 + 10 = 30
]

* Harmony bonus:

  * `A2` and `B1` both flavor `2` → `+10`

### Total:

[
30 + 10 = 40
]

---

## **Case 3**

### Input

```text id="xxuhms"
2
3
4
20
1 10
2 20
1 15
2 25
3 70
```

### Output

```text id="y7i24u"
140
```

### Explanation

One optimal merged sequence is:

```text id="hfd9wb"
A1 -> B1 -> B2 -> B3
```

Flavors:

```text id="bzzs4i"
1 -> 1 -> 2 -> 3
```

### Score:

* Intensity sum:

[
10 + 15 + 25 + 70 = 120
]

* Harmony bonus:

  * `A1` and `B1` both flavor `1` → `+20`

### Total:

[
120 + 20 = 140
]

---

# 💡 Core Idea

This is **not** a simple greedy problem.

Because:

* You can choose from **either A or B**
* You must preserve order in both arrays
* Bonus depends on the **last selected flavor**
* Need **exactly K selections**

So this becomes a **Dynamic Programming on merged sequences** problem.

---

# 🧠 DP Approach

We define DP based on:

* how many spices taken from `A`
* how many spices taken from `B`
* total number of selected spices
* which collection the **last selected spice** came from

This is important because when choosing the next spice, we need to compare its flavor with the **last selected spice** to decide whether harmony bonus applies.

---

# ✅ State Definition

Let:

* `dpA[i][j]` = maximum score after selecting:

  * first `i` spices from A
  * first `j` spices from B
  * total selected = `i + j`
  * **last selected spice came from A**

* `dpB[i][j]` = same, but **last selected spice came from B**

We only keep states where:

[
i + j \le K
]

---

# 🔁 Transitions

Suppose current state is `(i, j)`.

---

## If next spice is from A

We move to:

[
(i+1, j)
]

Score added:

* intensity of `A[i]`
* plus harmony bonus if its flavor matches the previous spice flavor

So:

### From A → A

```text id="5m3hlj"
dpA[i+1][j] = max(dpA[i+1][j], dpA[i][j] + intensity(A[i]) + bonus_if_same)
```

### From B → A

```text id="e8fcd9"
dpA[i+1][j] = max(dpA[i+1][j], dpB[i][j] + intensity(A[i]) + bonus_if_same)
```

---

## If next spice is from B

We move to:

[
(i, j+1)
]

### From A → B

```text id="6v76k0"
dpB[i][j+1] = max(dpB[i][j+1], dpA[i][j] + intensity(B[j]) + bonus_if_same)
```

### From B → B

```text id="vkkxk8"
dpB[i][j+1] = max(dpB[i][j+1], dpB[i][j] + intensity(B[j]) + bonus_if_same)
```

---

# 🚀 Initialization

We can start by selecting:

* `A[0]` as the first spice
* or `B[0]` as the first spice

No harmony bonus is added for the first selected spice.

---

# ⏱ Time Complexity

We process all valid `(i, j)` where:

[
i + j \le K
]

So complexity is roughly:

[
O(K^2)
]

Which is efficient enough for interview-style constraints if implemented carefully.

---

# 👨‍💻 Java Solution

```java id="c5rkza"
import java.util.*;

public class Main {

    static final long NEG = Long.MIN_VALUE / 4;

    public static long MaxScore(int N, int M, int K, int H, List<List<Integer>> A, List<List<Integer>> B) {
        long[][] dpA = new long[K + 1][K + 1];
        long[][] dpB = new long[K + 1][K + 1];

        for (int i = 0; i <= K; i++) {
            Arrays.fill(dpA[i], NEG);
            Arrays.fill(dpB[i], NEG);
        }

        // Start from A
        if (N > 0 && K >= 1) {
            dpA[1][0] = A.get(0).get(1);
        }

        // Start from B
        if (M > 0 && K >= 1) {
            dpB[0][1] = B.get(0).get(1);
        }

        for (int i = 0; i <= K; i++) {
            for (int j = 0; j <= K; j++) {
                if (i + j >= K) continue;

                // Last from A
                if (i > 0 && dpA[i][j] != NEG) {
                    int lastFlavor = A.get(i - 1).get(0);

                    // Take next from A
                    if (i < N) {
                        int newFlavor = A.get(i).get(0);
                        int val = A.get(i).get(1);
                        long bonus = (newFlavor == lastFlavor) ? H : 0;
                        dpA[i + 1][j] = Math.max(dpA[i + 1][j], dpA[i][j] + val + bonus);
                    }

                    // Take next from B
                    if (j < M) {
                        int newFlavor = B.get(j).get(0);
                        int val = B.get(j).get(1);
                        long bonus = (newFlavor == lastFlavor) ? H : 0;
                        dpB[i][j + 1] = Math.max(dpB[i][j + 1], dpA[i][j] + val + bonus);
                    }
                }

                // Last from B
                if (j > 0 && dpB[i][j] != NEG) {
                    int lastFlavor = B.get(j - 1).get(0);

                    // Take next from A
                    if (i < N) {
                        int newFlavor = A.get(i).get(0);
                        int val = A.get(i).get(1);
                        long bonus = (newFlavor == lastFlavor) ? H : 0;
                        dpA[i + 1][j] = Math.max(dpA[i + 1][j], dpB[i][j] + val + bonus);
                    }

                    // Take next from B
                    if (j < M) {
                        int newFlavor = B.get(j).get(0);
                        int val = B.get(j).get(1);
                        long bonus = (newFlavor == lastFlavor) ? H : 0;
                        dpB[i][j + 1] = Math.max(dpB[i][j + 1], dpB[i][j] + val + bonus);
                    }
                }
            }
        }

        long ans = 0;
        for (int i = 0; i <= K; i++) {
            int j = K - i;
            if (j >= 0 && j <= K) {
                ans = Math.max(ans, dpA[i][j]);
                ans = Math.max(ans, dpB[i][j]);
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = Integer.parseInt(scan.nextLine().trim());
        int M = Integer.parseInt(scan.nextLine().trim());
        int K = Integer.parseInt(scan.nextLine().trim());
        int H = Integer.parseInt(scan.nextLine().trim());

        List<List<Integer>> A = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] parts = scan.nextLine().trim().split(" ");
            A.add(Arrays.asList(Integer.parseInt(parts[0]), Integer.parseInt(parts[1])));
        }

        List<List<Integer>> B = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            String[] parts = scan.nextLine().trim().split(" ");
            B.add(Arrays.asList(Integer.parseInt(parts[0]), Integer.parseInt(parts[1])));
        }

        System.out.println(MaxScore(N, M, K, H, A, B));
    }
}
```

---

# 🐍 Python Solution

```python id="8r86ng"
NEG = -10**18

def max_score(N, M, K, H, A, B):
    dpA = [[NEG] * (K + 1) for _ in range(K + 1)]
    dpB = [[NEG] * (K + 1) for _ in range(K + 1)]

    if N > 0 and K >= 1:
        dpA[1][0] = A[0][1]

    if M > 0 and K >= 1:
        dpB[0][1] = B[0][1]

    for i in range(K + 1):
        for j in range(K + 1):
            if i + j >= K:
                continue

            if i > 0 and dpA[i][j] != NEG:
                last_flavor = A[i - 1][0]

                if i < N:
                    nf, val = A[i]
                    bonus = H if nf == last_flavor else 0
                    dpA[i + 1][j] = max(dpA[i + 1][j], dpA[i][j] + val + bonus)

                if j < M:
                    nf, val = B[j]
                    bonus = H if nf == last_flavor else 0
                    dpB[i][j + 1] = max(dpB[i][j + 1], dpA[i][j] + val + bonus)

            if j > 0 and dpB[i][j] != NEG:
                last_flavor = B[j - 1][0]

                if i < N:
                    nf, val = A[i]
                    bonus = H if nf == last_flavor else 0
                    dpA[i + 1][j] = max(dpA[i + 1][j], dpB[i][j] + val + bonus)

                if j < M:
                    nf, val = B[j]
                    bonus = H if nf == last_flavor else 0
                    dpB[i][j + 1] = max(dpB[i][j + 1], dpB[i][j] + val + bonus)

    ans = 0
    for i in range(K + 1):
        j = K - i
        if 0 <= j <= K:
            ans = max(ans, dpA[i][j], dpB[i][j])

    return ans


N = int(input().strip())
M = int(input().strip())
K = int(input().strip())
H = int(input().strip())

A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(M)]

print(max_score(N, M, K, H, A, B))
```

---

# 💭 Hints for Students

### Hint 1

This is like **merging two ordered arrays**, but with a scoring condition.

### Hint 2

At every step, you can only take the **next unused element** from A or B.

### Hint 3

The harmony bonus depends only on the **previous selected spice**.

### Hint 4

So DP must remember:

* how many taken from A
* how many taken from B
* where the last spice came from

---

# 🎯 Interview Questions Based on This Problem

Students should be ready for these:

## Conceptual

* Why is this not a greedy problem?
* Why do we need to track the **last selected source**?
* Why can’t normal subsequence DP solve this directly?

## Follow-up Variants

* What if harmony bonus depends on **same intensity** instead of same flavor?
* What if the bonus is based on **difference ≤ X**?
* What if we must select **at least one spice from each collection**?
* What if there are **3 collections instead of 2**?

## Optimization Discussion

* Can this be optimized in memory?
* Can we reconstruct the actual optimal sequence?

---

# 🔗 Similar Practice Links (Active)

## **LeetCode**

* [Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/)
* [Interleaving String](https://leetcode.com/problems/interleaving-string/)
* [Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/)

## **GeeksforGeeks**

* [Dynamic Programming on Subsequences](https://www.geeksforgeeks.org/dynamic-programming-dp-on-arrays-tutorial/)
* [Interleaving Strings](https://www.geeksforgeeks.org/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/)

## **Codeforces**

* [DP Problemset](https://codeforces.com/problemset?tags=dp)
* [Constructive + DP Practice](https://codeforces.com/problemset?tags=dp,implementation)

---

# 📌 Best Sheet Label

```text id="9g8g4x"
Hard — Ordered Merge DP with Adjacency Bonus
```

---

