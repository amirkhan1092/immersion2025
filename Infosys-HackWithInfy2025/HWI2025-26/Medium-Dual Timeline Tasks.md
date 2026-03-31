
---

# 🟡 **Dual Timeline Tasks**

## 🧩 Problem Statement

A city maintenance department has **N repair tasks** that must be completed.

Each task `i` has:

* `D[i]` → the **time required** to complete the task
* `P[i]` → the **penalty weight** associated with the task

The department has **two repair teams**, **Team A** and **Team B**, working in parallel.

### Rules:

* Tasks must be processed in the **given order**
* Each task must be assigned to **exactly one team**
* Once assigned, each team completes its tasks **sequentially**
* If a task finishes at time `T`, its penalty cost is:

[
T \times P[i]
]

The **total penalty** is the sum of penalties of all tasks.

### Goal:

Find the **minimum possible total penalty** by optimally assigning tasks between the two teams.

---

# 📥 Input Format

* The first line contains an integer `N`, denoting the number of tasks.
* The next `N` lines each contain an integer describing `D[i]`.
* The next `N` lines each contain an integer describing `P[i]`.

---

# 📌 Constraints

[
1 \le N \le 10^2
]

[
1 \le D[i] \le 10^3
]

[
1 \le P[i] \le 10^3
]

---

# 📤 Output Format

* Print a single integer — the **minimum total penalty**.

---

# 🧪 Sample Test Cases

---

## **Case 1**

### Input

```text
2
3
3
5
4
```

### Output

```text
27
```

### Explanation

Assign:

* Task 1 → Team A
* Task 2 → Team B

Now compute:

**Team A**

* Task 1 finishes at time `3`
* Penalty = `3 × 5 = 15`

**Team B**

* Task 2 finishes at time `3`
* Penalty = `3 × 4 = 12`

Total penalty:

[
15 + 12 = 27
]

Minimum = **27**

---

## **Case 2**

### Input

```text
3
4
1
2
2
3
1
```

### Output

```text
14
```

### Explanation

Assign:

* Task 1 → Team A
* Task 2 → Team B
* Task 3 → Team B

Now compute:

**Team A**

* Task 1 → finishes at `4`
* Penalty = `4 × 2 = 8`

**Team B**

* Task 2 → finishes at `1`
* Penalty = `1 × 3 = 3`
* Task 3 → finishes at `1 + 2 = 3`
* Penalty = `3 × 1 = 3`

Total penalty:

[
8 + 3 + 3 = 14
]

Minimum = **14**

---

## **Case 3**

### Input

```text
3
2
2
2
1
2
3
```

### Output

```text
16
```

### Explanation

Assign:

* Task 1 → Team A
* Task 2 → Team A
* Task 3 → Team B

Now compute:

**Team A**

* Task 1 → finishes at `2`
* Penalty = `2 × 1 = 2`
* Task 2 → finishes at `2 + 2 = 4`
* Penalty = `4 × 2 = 8`

**Team B**

* Task 3 → finishes at `2`
* Penalty = `2 × 3 = 6`

Total penalty:

[
2 + 8 + 6 = 16
]

Minimum = **16**

---

# 💡 Key Insight

Each task must go to either:

* **Team A**
* **Team B**

If we know how much total time has already been used by one team, we automatically know the other team’s time too.

So this becomes a **Dynamic Programming on prefix + current load** problem.

---

# 🧠 Expected Approach

## **DP State**

Let:

[
dp[i][t]
]

= minimum penalty after assigning first `i` tasks, where **Team A** has total time `t`.

Then Team B time can be derived from the total durations assigned so far.

For each task, we have two choices:

### Choice 1:

Assign task `i` to **Team A**

### Choice 2:

Assign task `i` to **Team B**

Update penalty accordingly.

---

# ⏱ Complexity

If total duration sum is `S`, then:

* **Time Complexity:** `O(N × S)`
* **Space Complexity:** `O(S)` with optimization

Since:

[
N \le 100,; D[i] \le 1000
]

This DP is feasible.

---

# 🎯 Topics Used

You can mention these in your practice sheet:

* **Dynamic Programming**
* **Knapsack-style DP**
* **Scheduling**
* **State Transition**
* **Optimization**

---

# 🎤 Interview Questions Based on This Problem

Students should be ready to answer:

### Conceptual

* Why can this be solved using DP?
* What is the state?
* Why do we only need one team’s time in the DP state?

### Optimization

* Can you reduce space from `O(N*S)` to `O(S)`?
* Why is greedy not always correct here?

### Follow-up Variants

* What if there were **3 teams** instead of 2?
* What if tasks could be reordered?
* What if each team had a different speed?

---

# 👨‍💻 Java Solution (Clean DP)

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] D = new int[N];
        int[] P = new int[N];

        int totalDuration = 0;

        for (int i = 0; i < N; i++) {
            D[i] = sc.nextInt();
            totalDuration += D[i];
        }

        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt();
        }

        long INF = (long) 1e18;
        long[] dp = new long[totalDuration + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        int prefixSum = 0;

        for (int i = 0; i < N; i++) {
            long[] newDp = new long[totalDuration + 1];
            Arrays.fill(newDp, INF);

            for (int tA = 0; tA <= prefixSum; tA++) {
                if (dp[tA] == INF) continue;

                int tB = prefixSum - tA;

                // Assign task i to Team A
                int newTA = tA + D[i];
                long costA = dp[tA] + (long) newTA * P[i];
                newDp[newTA] = Math.min(newDp[newTA], costA);

                // Assign task i to Team B
                int newTB = tB + D[i];
                long costB = dp[tA] + (long) newTB * P[i];
                newDp[tA] = Math.min(newDp[tA], costB);
            }

            dp = newDp;
            prefixSum += D[i];
        }

        long ans = INF;
        for (long val : dp) {
            ans = Math.min(ans, val);
        }

        System.out.println(ans);
    }
}
```

---

# 🐍 Python Solution

```python
n = int(input())
D = [int(input()) for _ in range(n)]
P = [int(input()) for _ in range(n)]

total = sum(D)
INF = 10**18

dp = [INF] * (total + 1)
dp[0] = 0

prefix = 0

for i in range(n):
    new_dp = [INF] * (total + 1)

    for tA in range(prefix + 1):
        if dp[tA] == INF:
            continue

        tB = prefix - tA

        # Assign to Team A
        newTA = tA + D[i]
        new_dp[newTA] = min(new_dp[newTA], dp[tA] + newTA * P[i])

        # Assign to Team B
        newTB = tB + D[i]
        new_dp[tA] = min(new_dp[tA], dp[tA] + newTB * P[i])

    dp = new_dp
    prefix += D[i]

print(min(dp))
```

---

# 🔗 Similar Online Practice

This exact problem is custom/OA-style, but these are the **closest topic matches**:

### LeetCode

* [Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)
* [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)
* [Find Minimum Time to Finish All Jobs](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)

### GeeksforGeeks

* [Partition problem](https://www.geeksforgeeks.org/partition-problem-dp-18/)
* [Scheduling / DP based problems](https://www.geeksforgeeks.org/dynamic-programming/)

### Codeforces

* DP + scheduling + assignment style problems:

  * [https://codeforces.com/problemset?tags=dp](https://codeforces.com/problemset?tags=dp)
  * [https://codeforces.com/problemset?tags=greedy](https://codeforces.com/problemset?tags=greedy)

---

# 📌 Best Label for Practice Sheet

```text
Medium — DP + Scheduling + State Optimization
```

---


