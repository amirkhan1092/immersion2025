

# 🟡 **Problem — Emil’s Special Longest Common Sequence**

## **Difficulty Level**

**Medium**

## **Topics Used**

* Dynamic Programming
* Longest Common Subsequence (LCS)
* 2D DP
* String Matching
* DP State Design

---

# 🧩 Problem Statement

Emil has a particular fondness for the letter **`'e'`**.

He defines the **score** of a common subsequence between two strings based on two factors:

* The **total length** of the subsequence
* The **number of times** the letter **`'e'`** appears in that subsequence

The score is calculated as:

[
\text{Score} = (\text{Length of subsequence}) \times (\text{Number of occurrences of 'e'})
]

You are given two strings `A` and `B`.

Your task is to find the **maximum possible score** Emil can achieve by choosing an **optimal common subsequence** between the two strings.

---

# 📥 Input Format

* The first line contains a string `A`, denoting the first input string.
* The second line contains a string `B`, denoting the second input string.

---

# 📌 Constraints

[
1 \le |A| \le 500
]

[
1 \le |B| \le 500
]

* Both strings consist of lowercase English letters.

---

# 📤 Output Format

Print a single integer — the **maximum score** obtainable.

---

# 🧪 Sample Test Cases

---

## **Case 1**

### Input

```text id="x08s2n"
abcde
ace
```

### Output

```text id="6fmm7j"
3
```

### Explanation

Common subsequences include:

* `"ac"` → length = 2, number of `'e'` = 0 → score = 0
* `"ace"` → length = 3, number of `'e'` = 1 → score = 3

Maximum score = **3**

---

## **Case 2**

### Input

```text id="4ieyn7"
eeabc
eebc
```

### Output

```text id="ehlnrq"
8
```

### Explanation

One optimal common subsequence is:

```text id="8h9r0i"
eebc
```

* Length = 4
* Number of `'e'` = 2

Score:

[
4 \times 2 = 8
]

---

## **Case 3**

### Input

```text id="57v7ha"
abcd
xyz
```

### Output

```text id="c8s84c"
0
```

### Explanation

There is no meaningful common subsequence containing `'e'`.

Even if some common subsequence exists of length > 0 without `'e'`, score remains:

[
\text{length} \times 0 = 0
]

So answer = **0**

---

# 💡 Key Insight

This is **not just normal LCS**.

In normal LCS, we maximize only the **length**.

But here the score depends on **two values**:

1. **Length**
2. **Count of `'e'`**

And the final objective is:

[
\text{length} \times \text{countE}
]

So while building the common subsequence, we must carefully track both.

---

# 🧠 Approach

We use **Dynamic Programming**.

Let:

[
dp[i][j]
]

represent the **best possible states** considering:

* first `i` characters of `A`
* first `j` characters of `B`

But one value is not enough.
We need to know:

* what length we can form
* how many `'e'` characters are included

---

## Better DP Idea

We define:

[
dp[i][j][eCount] = \text{maximum length of a common subsequence using exactly } eCount \text{ e's}
]

Then at the end, for every possible `eCount`, compute:

[
\text{score} = dp[n][m][eCount] \times eCount
]

Take the maximum.

---

# ✅ Transition

For each pair `(i, j)`:

## If characters don’t match:

Skip one character from either string:

[
dp[i][j][e] = \max(dp[i-1][j][e], dp[i][j-1][e])
]

---

## If characters match:

Suppose:

[
A[i-1] = B[j-1] = ch
]

Then:

### If `ch == 'e'`

Taking this character increases:

* length by `1`
* count of `'e'` by `1`

[
dp[i][j][e] = \max(dp[i][j][e], dp[i-1][j-1][e-1] + 1)
]

---

### If `ch != 'e'`

Taking this character increases:

* length by `1`
* `'e'` count unchanged

[
dp[i][j][e] = \max(dp[i][j][e], dp[i-1][j-1][e] + 1)
]

---

# ⏱ Time Complexity

Let:

* `n = |A|`
* `m = |B|`
* maximum possible number of `'e'` = at most `min(n, m)`

So complexity:

[
O(n \cdot m \cdot E)
]

With constraints up to 500, this is acceptable with careful implementation.

---

# 👨‍💻 Java Solution

```java id="ljzndv"
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();

        int n = A.length();
        int m = B.length();
        int maxE = Math.min(n, m);

        int[][][] dp = new int[n + 1][m + 1][maxE + 1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                Arrays.fill(dp[i][j], -1000000);
            }
        }

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                dp[i][j][0] = 0;
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                for (int e = 0; e <= maxE; e++) {
                    dp[i][j][e] = Math.max(dp[i - 1][j][e], dp[i][j - 1][e]);

                    if (A.charAt(i - 1) == B.charAt(j - 1)) {
                        char ch = A.charAt(i - 1);

                        if (ch == 'e') {
                            if (e > 0) {
                                dp[i][j][e] = Math.max(dp[i][j][e], dp[i - 1][j - 1][e - 1] + 1);
                            }
                        } else {
                            dp[i][j][e] = Math.max(dp[i][j][e], dp[i - 1][j - 1][e] + 1);
                        }
                    }
                }
            }
        }

        int ans = 0;
        for (int e = 1; e <= maxE; e++) {
            if (dp[n][m][e] > 0) {
                ans = Math.max(ans, dp[n][m][e] * e);
            }
        }

        System.out.println(ans);
    }
}
```

---

# 🐍 Python Solution

```python id="5w45l2"
A = input().strip()
B = input().strip()

n, m = len(A), len(B)
maxE = min(n, m)

NEG = -10**9
dp = [[[NEG] * (maxE + 1) for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        dp[i][j][0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for e in range(maxE + 1):
            dp[i][j][e] = max(dp[i - 1][j][e], dp[i][j - 1][e])

            if A[i - 1] == B[j - 1]:
                ch = A[i - 1]
                if ch == 'e':
                    if e > 0:
                        dp[i][j][e] = max(dp[i][j][e], dp[i - 1][j - 1][e - 1] + 1)
                else:
                    dp[i][j][e] = max(dp[i][j][e], dp[i - 1][j - 1][e] + 1)

ans = 0
for e in range(1, maxE + 1):
    if dp[n][m][e] > 0:
        ans = max(ans, dp[n][m][e] * e)

print(ans)
```

---

# 💭 Hints for Students

### Hint 1

This is based on **LCS**, but normal LCS alone is not enough.

### Hint 2

Track not just the subsequence **length**, but also how many `'e'` are used.

### Hint 3

Try to think:

> “If I decide to include this matching character, what changes?”

### Hint 4

At the end, compute:

[
\text{length} \times \text{count of e}
]

---

# 🎯 Interview Discussion Points

Students should be able to answer:

## Core Questions

* Why is this **not** a simple LCS problem?
* What extra state do we need?
* Why do we track the number of `'e'` separately?

## Optimization Questions

* Can this be reduced from 3D DP to 2D rolling DP?
* What happens if the scoring formula changes to:

  * `length + countE`
  * `length² × countE`

## Follow-up Variants

* Replace `'e'` with any special character `X`
* Give different weights to different characters
* Find the actual subsequence, not just the score

---

# 🔗 Similar Practice Links (Active)

## **LeetCode**

* [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
* [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)
* [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

## **GeeksforGeeks**

* [Longest Common Subsequence | DP](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/)
* [Dynamic Programming on Strings](https://www.geeksforgeeks.org/dynamic-programming-dp-on-strings-tutorial/)

## **Codeforces**

* [DP on Strings Problemset](https://codeforces.com/problemset?tags=dp,strings)
* [LCS Related Practice](https://codeforces.com/problemset?tags=dp)

---

# 📌 Best Sheet Label

```text id="7ag3y8"
Medium — LCS Variant with Custom Scoring
```

---


