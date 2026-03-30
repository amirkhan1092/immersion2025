---

# 🟡 QUESTION 2 — MEDIUM

# **Coffee Shop Rewards**

---

## 🧩 Problem Statement

A coffee shop runs a loyalty reward program over `N` consecutive days.

On each day `i`, a reward worth `R[i]` points is available.

Each reward has a type:

* `type[i] = 0` → **Regular Reward**
* `type[i] = 1` → **Premium Reward**

You may claim **at most one reward per day**.

---

## 📜 Rules

### ☕ Regular Reward

If you claim a regular reward on day `i`:

* You can still claim reward on day `i+1`

### ⭐ Premium Reward

If you claim a premium reward on day `i`:

* You **cannot claim** any reward on:

  * day `i+1`
  * day `i+2`

The next available claim day becomes `i+3`

### ⏭️ Skipping

You may skip any day.

---

## 🎯 Goal

Find the **maximum total reward points** possible.

---

## 📥 Input Format

* First line: integer `N`
* Next `N` lines: `R[i]`
* Next `N` lines: `type[i]`

This exact problem description and sample cases are visible in the PDF pages for the Medium section 

---

## 📌 Constraints

* `1 <= N <= 10^5`
* `1 <= R[i] <= 10^4`
* `0 <= type[i] <= 1`

---

## 📤 Sample Input 1

```text
3
5
5
5
0
0
0
```

## 📤 Sample Output 1

```text
15
```

### ✅ Explanation

All rewards are regular, so claim all:

`5 + 5 + 5 = 15`

---

## 📤 Sample Input 2

```text
4
10
20
30
40
1
1
1
1
```

## 📤 Sample Output 2

```text
50
```

### ✅ Explanation

All are premium.

Best choice:

* Claim day 1 → `10`
* Skip day 2, 3
* Claim day 4 → `40`

Total = `50`

---

## 📤 Sample Input 3

```text
4
10
100
10
10
0
1
0
0
```

## 📤 Sample Output 3

```text
110
```

### ✅ Explanation

Best:

* Claim day 1 → `10`
* Claim day 2 (premium) → `100`
* Then day 3 and 4 blocked

Total = `110`

---

# 🔍 Core Idea

At every day, you have two choices:

1. **Skip**
2. **Take reward**

This is a classic **Dynamic Programming** problem.

---

# 🧠 DP State

Let:

[
dp[i] = \text{maximum reward from day } i \text{ to } N-1
]

---

# 🔁 Transition

## Case 1: Skip current day

[
dp[i] = dp[i+1]
]

## Case 2: Take reward on day `i`

### If Regular (`type[i] = 0`)

[
take = R[i] + dp[i+1]
]

### If Premium (`type[i] = 1`)

[
take = R[i] + dp[i+3]
]

So:

[
dp[i] = \max(skip, take)
]

---

# ✅ Approach

Start from the last day and move backwards.

---

# ⏱️ Time Complexity

* Time: `O(N)`
* Space: `O(N)`

Can also be optimized.

---

# 💡 Hints for Students

### Hint 1

Think: **Take or Skip**

### Hint 2

Premium reward behaves like a **cooldown**

### Hint 3

This is similar to:

* House Robber
* Stock cooldown DP

---

# 🎤 Interview Questions

* Why is greedy not enough?
* Can we optimize space?
* What if premium blocks `k` future days?
* What if there are 3 reward types?

---

# ✅ Java Solution

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        long[] R = new long[N];
        int[] type = new int[N];

        for (int i = 0; i < N; i++) R[i] = sc.nextLong();
        for (int i = 0; i < N; i++) type[i] = sc.nextInt();

        long[] dp = new long[N + 3];

        for (int i = N - 1; i >= 0; i--) {
            long skip = dp[i + 1];
            long take;

            if (type[i] == 0) {
                take = R[i] + dp[i + 1];
            } else {
                take = R[i] + dp[i + 3];
            }

            dp[i] = Math.max(skip, take);
        }

        System.out.println(dp[0]);
    }
}
```

---

---
