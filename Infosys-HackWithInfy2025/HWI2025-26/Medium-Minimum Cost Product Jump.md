

# 🟡 **Problem — Minimum Cost Product Jump**

## **Difficulty Level**

**Medium**

## **Topics Used**

* Dynamic Programming
* Sliding Window DP
* Array Traversal
* Optimization
* State Transition

---

# 🧩 Problem Statement

You are given an array `A` of `N` integers and an integer `K`.

You start at **index 0** and must reach **index N - 1**.

From any index `i`, you may jump to any index `j` such that:

[
i < j \le i + K
]

The **cost** of jumping from index `i` to index `j` is:

[
A[i] \times A[j]
]

Your task is to find the **minimum total cost** required to reach the **last index**.

---

# 📥 Input Format

* The first line contains an integer `N`, denoting the size of the array.
* The second line contains an integer `K`, denoting the maximum jump length.
* The next `N` lines each contain one integer representing `A[i]`.

---

# 📌 Constraints

[
1 \le N \le 10^5
]

[
1 \le K \le 10^2
]

[
-10^5 \le A[i] \le 10^5
]

---

# 📤 Output Format

Print a single integer — the **minimum total cost** to reach index `N - 1`.

---

# 🧪 Sample Test Cases

---

## **Case 1**

### Input

```text
4
2
2
-1
3
4
```

### Output

```text
-6
```

### Explanation

Possible jumps:

* `0 → 1`: cost = `2 × (-1) = -2`
* `0 → 2`: cost = `2 × 3 = 6`

From index `1`:

* `1 → 2`: cost = `(-1) × 3 = -3`
* `1 → 3`: cost = `(-1) × 4 = -4`

From index `2`:

* `2 → 3`: cost = `3 × 4 = 12`

Now evaluate paths:

### Path 1:

`0 → 1 → 2 → 3`

Cost:

[
-2 + (-3) + 12 = 7
]

### Path 2:

`0 → 1 → 3`

Cost:

[
-2 + (-4) = -6
]

### Path 3:

`0 → 2 → 3`

Cost:

[
6 + 12 = 18
]

Minimum cost = **-6**

---

## **Case 2**

*(partially visible in image, so use as custom practice format)*

### Example Input

```text
5
3
-2
5
1
-4
2
```

### Example Output

```text
-18
```

### Explanation

One optimal path can be:

`0 → 3 → 4`

Cost:

[
(-2 \times -4) + (-4 \times 2) = 8 + (-8) = 0
]

Another path:

`0 → 1 → 3 → 4`

Cost:

[
(-2 \times 5) + (5 \times -4) + (-4 \times 2)
]

[
= -10 + (-20) + (-8) = -38
]

Minimum valid path depends on `K = 3`.

---

# 💡 Key Observation

To reach index `i`, you can only come from the previous **K indices**.

So define:

[
dp[i] = \text{minimum cost to reach index } i
]

Then:

[
dp[i] = \min_{j \in [i-K, i-1]} \left(dp[j] + A[j] \times A[i]\right)
]

This is a classic **DP with limited transition window** problem.

---

# 🧠 Approach

## Step 1

Initialize:

[
dp[0] = 0
]

because we start at index `0` with no cost.

## Step 2

For every index `i` from `1` to `N-1`, check all valid previous indices:

[
j \in [\max(0, i-K), i-1]
]

Update:

[
dp[i] = \min(dp[i], dp[j] + A[j] \times A[i])
]

## Step 3

Final answer:

[
dp[N-1]
]

---

# ⏱ Time Complexity

Since for each index we check at most `K` previous positions:

[
O(N \times K)
]

With:

* `N ≤ 10^5`
* `K ≤ 100`

This is efficient enough.

---

# ✅ Optimality

This is the best practical solution for the given constraints because:

* `K` is small
* Each state depends only on the previous `K` states

---

# 👨‍💻 Java Solution

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        long[] A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextLong();
        }

        long INF = Long.MAX_VALUE / 4;
        long[] dp = new long[N];
        Arrays.fill(dp, INF);

        dp[0] = 0;

        for (int i = 1; i < N; i++) {
            for (int j = Math.max(0, i - K); j < i; j++) {
                dp[i] = Math.min(dp[i], dp[j] + A[j] * A[i]);
            }
        }

        System.out.println(dp[N - 1]);
    }
}
```

---

# 🐍 Python Solution

```python
n = int(input())
k = int(input())
A = [int(input()) for _ in range(n)]

INF = 10**18
dp = [INF] * n
dp[0] = 0

for i in range(1, n):
    for j in range(max(0, i - k), i):
        dp[i] = min(dp[i], dp[j] + A[j] * A[i])

print(dp[-1])
```

---

# 💭 Hints for Students

### Hint 1

Think in terms of **minimum cost to reach each index**.

### Hint 2

From index `i`, you only need to look back at the **previous K positions**.

### Hint 3

This is not greedy — you need **DP**.

### Hint 4

Negative numbers can reduce total cost, so be careful.

---

# 🎤 Interview Questions Based on This Problem

Students should be ready to answer:

### Conceptual

* Why is this a **DP problem**?
* What does `dp[i]` represent?
* Why does greedy fail here?

### Technical

* What is the recurrence relation?
* Why is the time complexity `O(N*K)`?
* Can this be optimized further if `K` becomes very large?

### Follow-up Variants

* What if each jump also had a fixed extra cost?
* What if you could jump **backward** too?
* What if the jump cost was `|A[i] - A[j]|` instead of product?

---

# 🔗 Similar Practice Links (Active)

## **LeetCode**

* [Jump Game VI](https://leetcode.com/problems/jump-game-vi/)
* [Frog Jump](https://leetcode.com/problems/frog-jump/)
* [Minimum Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

## **GeeksforGeeks**

* [Min Cost Path](https://www.geeksforgeeks.org/min-cost-path-dp-6/)
* [Dynamic Programming Introduction](https://www.geeksforgeeks.org/dynamic-programming/)

## **Codeforces**

* [DP Problemset](https://codeforces.com/problemset?tags=dp)
* [Greedy + DP Practice](https://codeforces.com/problemset?tags=dp,greedy)

---

# 📌 Best Sheet Label

```text
Medium — DP on Array with Limited Jumps
```

---

