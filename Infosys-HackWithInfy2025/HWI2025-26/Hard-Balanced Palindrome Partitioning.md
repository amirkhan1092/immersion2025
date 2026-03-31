

# 🔴 **Problem — Balanced Palindrome Partitioning**

---

## **Difficulty Level**

**Hard**

## **Topics Used**

* Dynamic Programming (DP)
* Palindrome DP / Preprocessing
* Binary Search on Answer
* String Partitioning
* Optimization DP
* Interval / Substring Logic

---

# 🧩 Problem Statement

You are given:

* a string `S` of length `N`
* an integer `K`

A **palindrome** is a string that reads the same forward and backward, such as:

```text id="1v8jgm"
"aba", "racecar", "zz"
```

You need to partition the entire string `S` into **contiguous substrings** such that:

* **at least `K`** of those substrings are palindromes

Among all such valid partitions, define the **balance** as:

> the **length of the shortest substring** in that partition.

---

# 🎯 Goal

Find the **maximum possible value** of:

[
\text{length of the shortest substring}
]

across all valid partitions that contain at least `K` palindromic substrings.

---

## 📌 Important Note

You only need to output the **maximum possible shortest-substring length**.

You do **not** need to output the partition itself.

Also, a valid partition always exists for `K <= N`, because every single character is a palindrome.

---

# 📥 Input Format

* First line: string `S`
* Second line: integer `K`

---

# 📌 Constraints

The lower half of the image is not visible, but this kind of problem is usually intended for:

[
1 \le N \le 500 \text{ or } 1000
]

[
1 \le K \le N
]

---

# 📤 Output Format

Print one integer:

```text id="j5o2g1"
Maximum possible value of the shortest substring length
```

---

# 🧪 Example

Since the sample section is not visible in the screenshot, here is a **clean representative example**.

---

## **Sample Input**

```text id="y17pfx"
abacdc
2
```

## **Sample Output**

```text id="syw3rz"
3
```

---

## **Explanation**

Possible partition:

```text id="zjv7ol"
"aba" | "cdc"
```

Both substrings are palindromes.

* Number of palindromic substrings = `2` ✔
* Shortest substring length = `3`

This is optimal.

So answer = **3**

---

# 💡 Core Idea

We want to maximize:

[
\min(\text{substring lengths in the partition})
]

This is a classic:

# 👉 **Binary Search on Answer**

We guess a value `L`:

> “Can we partition the string such that every part has length at least `L`, and at least `K` of the parts are palindromes?”

If yes → try bigger `L`

If no → try smaller `L`

---

# 🧠 Full Approach

The solution has **2 major steps**:

---

# Step 1 — Precompute all palindromes

We need to quickly know:

> Is substring `S[i..j]` a palindrome?

Use DP:

[
pal[i][j] = \text{true if } S[i..j] \text{ is palindrome}
]

### Transition:

* Length 1 → palindrome
* Length 2 → palindrome if `S[i] == S[j]`
* Length > 2 → palindrome if:

  * `S[i] == S[j]`
  * and `pal[i+1][j-1] = true`

This takes:

[
O(N^2)
]

---

# Step 2 — Binary Search on minimum allowed part length

Suppose we fix a candidate minimum length = `L`.

Now ask:

> Can we partition the whole string into pieces of length **at least `L`**, such that at least `K` of them are palindromes?

---

# Step 3 — DP Feasibility Check

Let:

[
dp[i] = \text{maximum number of palindromic substrings we can get while partitioning } S[0..i-1]
]

If position `j → i-1` forms a valid piece:

* its length is at least `L`
* if palindrome → contributes `+1`
* else contributes `0`

Transition:

[
dp[i] = \max(dp[i], dp[j] + (pal[j][i-1] ? 1 : 0))
]

for all valid `j`.

If at the end:

[
dp[N] \ge K
]

then `L` is feasible.

---

# ✅ Why This Works

We are maximizing the **minimum substring length**, which is a monotonic property:

* If length `L` is possible,
* then all smaller lengths are also possible.

That makes **binary search valid**.

And DP ensures we compute the best number of palindrome parts under that restriction.

---

# ⏱ Time Complexity

## Palindrome preprocessing:

[
O(N^2)
]

## Binary Search:

[
O(\log N)
]

## Feasibility DP per check:

[
O(N^2)
]

## Total:

[
O(N^2 \log N)
]

This is efficient for typical constraints.

---

# 👨‍💻 Java Solution

```java id="vh0a4x"
import java.util.*;

public class Main {

    static boolean[][] buildPalindromeTable(String s) {
        int n = s.length();
        boolean[][] pal = new boolean[n][n];

        for (int len = 1; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;

                if (len == 1) {
                    pal[i][j] = true;
                } else if (len == 2) {
                    pal[i][j] = (s.charAt(i) == s.charAt(j));
                } else {
                    pal[i][j] = (s.charAt(i) == s.charAt(j)) && pal[i + 1][j - 1];
                }
            }
        }

        return pal;
    }

    static boolean canAchieve(String s, int K, int minLen, boolean[][] pal) {
        int n = s.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1000000);
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int len = i - j;
                if (len >= minLen && dp[j] > -1000000) {
                    int add = pal[j][i - 1] ? 1 : 0;
                    dp[i] = Math.max(dp[i], dp[j] + add);
                }
            }
        }

        return dp[n] >= K;
    }

    static int maxBalancedLength(String s, int K) {
        int n = s.length();
        boolean[][] pal = buildPalindromeTable(s);

        int low = 1, high = n, ans = 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (canAchieve(s, K, mid, pal)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine().trim();
        int K = Integer.parseInt(sc.nextLine().trim());

        System.out.println(maxBalancedLength(s, K));
    }
}
```

---

# 🐍 Python Solution

```python id="52vlw5"
def build_palindrome_table(s):
    n = len(s)
    pal = [[False] * n for _ in range(n)]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if length == 1:
                pal[i][j] = True
            elif length == 2:
                pal[i][j] = (s[i] == s[j])
            else:
                pal[i][j] = (s[i] == s[j]) and pal[i + 1][j - 1]

    return pal


def can_achieve(s, K, min_len, pal):
    n = len(s)
    NEG = -10**9
    dp = [NEG] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if i - j >= min_len and dp[j] != NEG:
                add = 1 if pal[j][i - 1] else 0
                dp[i] = max(dp[i], dp[j] + add)

    return dp[n] >= K


def max_balanced_length(s, K):
    n = len(s)
    pal = build_palindrome_table(s)

    low, high = 1, n
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        if can_achieve(s, K, mid, pal):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


s = input().strip()
K = int(input().strip())

print(max_balanced_length(s, K))
```

---

# 💭 Hints for Students

### Hint 1

Can you directly maximize the shortest substring length?

### Hint 2

Try checking if a fixed minimum length `L` is possible.

### Hint 3

You need fast palindrome checking for any substring.

### Hint 4

This is:

* **Palindrome DP**
* * **Partition DP**
* * **Binary Search on Answer**

---

# ❌ Common Mistakes

Students may do these mistakes:

* Recomputing palindrome checks again and again → TLE
* Forgetting that **non-palindrome parts are allowed**
* Assuming exactly `K` palindrome parts instead of **at least `K`**
* Doing brute-force partition generation
* Mixing “minimum substring length” with “number of parts”

---

# 🎯 Interview Questions Based on This Problem

## Conceptual

* Why is binary search applicable here?
* What makes this a monotonic feasibility problem?
* Why do we need palindrome preprocessing?

## Follow-up Variants

* What if **all** parts must be palindromes?
* What if you want **exactly `K`** palindromic substrings?
* What if you want to **minimize number of cuts**?
* What if partition cost depends on substring length?

## Coding Variants

* Print one optimal partition
* Count number of valid partitions
* Maximize shortest palindrome only (all parts palindrome)

---

# 🔗 Similar Practice Links (Active)

## **LeetCode**

* [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
* [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)
* [Partition Labels](https://leetcode.com/problems/partition-labels/) *(partition thinking)*

## **GeeksforGeeks**

* [Palindrome Partitioning DP](https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/)
* [Binary Search on Answer](https://www.geeksforgeeks.org/binary-search-on-answer-tutorial-with-problems/)

## **Codeforces**

* [Palindrome Problems](https://codeforces.com/problemset?tags=palindrome)
* [DP Problemset](https://codeforces.com/problemset?tags=dp)

---

# 📌 Best Sheet Label

```text id="15g9jv"
Hard — Binary Search on Answer + Palindrome Partition DP
```

---

# 📝 One-Line Student Understanding

> “Binary search the minimum allowed part length, then use DP to check whether the whole string can still be partitioned with at least K palindrome pieces.”

---

