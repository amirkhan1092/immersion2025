

# EASY

# **Coin Operations**

---

## 🧩 Problem Statement

You are given an integer `N`, and two arrays `A` and `B`, each of size `N`.

For every index `i`, you start with **0 coins** and repeatedly perform operations until both `A[i]` and `B[i]` become **0**.

### Allowed Operations

For each index `i`:

* If `A[i] > 0`:

  * Add **1 coin**
  * Decrease `A[i]` by `1`

* If `B[i] > 0`:

  * Multiply your current coins by `2`
  * Decrease `B[i]` by `1`

You may perform the operations in **any order** for that index.

---

## 🎯 Goal

For each `i`, let `cost[i]` be the **maximum possible number of coins** you can obtain after reducing both `A[i]` and `B[i]` to zero.

Return:

[
\sum cost[i] \mod (10^9+7)
]

---

## 📥 Input Format

* First line contains an integer `N`
* Next `N` lines contain `A[i]`
* Next `N` lines contain `B[i]`

---

## 📌 Constraints

* `1 <= N <= 5 * 10^5`
* `1 <= A[i] <= 10^9`
* `1 <= B[i] <= 10^9`

These constraints are visible in the PDF screenshots for the Easy problem section 

---

## 📤 Sample Input 1

```text
1
1
1
```

## 📤 Sample Output 1

```text
2
```

### ✅ Explanation

For `A=1, B=1`

Best order:

1. Add 1 coin → `1`
2. Multiply by 2 → `2`

Final = `2`

---

## 📤 Sample Input 2

```text
1
1
2
```

## 📤 Sample Output 2

```text
4
```

### ✅ Explanation

Best order:

1. Add 1 → `1`
2. Multiply → `2`
3. Multiply → `4`

Final = `4`

---

# 🔍 Key Observation

To maximize coins:

✅ Perform **all +1 operations first**
✅ Then perform **all ×2 operations**

Because multiplication is more powerful **after** accumulation.

So for each index:

[
cost[i] = A[i] \times 2^{B[i]}
]

---

# 🧠 Approach

For each `i`:

1. Start with `A[i]` additions → coins = `A[i]`
2. Apply `B[i]` doublings:

[
coins = A[i] \cdot 2^{B[i]}
]

3. Add to answer modulo `10^9+7`

---

# ✅ Optimized Solution Idea

Use **fast modular exponentiation** for:

[
2^{B[i]} \mod (10^9+7)
]

---

# ⏱️ Time Complexity

* For each index: `O(log B[i])`
* Total:

[
O(N \log B_{max})
]

---

# 💡 Hints for Students

### Hint 1

Try small examples manually.

### Hint 2

Compare:

* `+1, +1, ×2`
  vs
* `×2, +1, +1`

### Hint 3

Which order gives bigger result?

---

# 🎤 Interview Questions

* Why should all additions happen before multiplications?
* Can greedy be formally proven here?
* Why do we need modular exponentiation?
* What if multiplication factor was `3` instead of `2`?

---

# ✅ Java Solution

```java
import java.util.*;

public class Main {
    static final long MOD = 1000000007L;

    static long power(long base, long exp) {
        long result = 1;
        base %= MOD;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        long[] A = new long[N];
        long[] B = new long[N];

        for (int i = 0; i < N; i++) A[i] = sc.nextLong();
        for (int i = 0; i < N; i++) B[i] = sc.nextLong();

        long ans = 0;

        for (int i = 0; i < N; i++) {
            long val = (A[i] % MOD) * power(2, B[i]) % MOD;
            ans = (ans + val) % MOD;
        }

        System.out.println(ans);
    }
}
```

---
