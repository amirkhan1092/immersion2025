
---

# 🟢 **Easy — String Stability Boost**

---

## 🧩 **Problem Statement**

You are given a string `S` consisting of lowercase English letters.

The **stability score** of the string is defined as the number of **distinct adjacent pairs** present in the string.

An adjacent pair is formed by characters at positions:

[
(S[i], S[i+1]) \quad \text{for } 0 \le i < |S|-1
]

You are allowed to perform **exactly one adjacent swap**, i.e., choose an index `i` and swap:

[
S[i] \text{ and } S[i+1]
]

Your task is to find the **maximum possible stability score** after performing **exactly one adjacent swap**.

---

# 🎯 **Goal**

Return the **maximum number of distinct adjacent pairs** that can appear in the string after exactly one adjacent swap.

---

# 📥 **Input Format**

* The first line contains a string `S`, denoting the given lowercase string.

---

# 📌 **Constraints**

[
1 \le |S| \le 10^3
]

---

# 📤 **Output Format**

* Print a single integer — the maximum possible stability score after exactly one adjacent swap.

---

# 🧪 **Sample Test Cases**

---

## **Sample Case 1**

### **Input**

```text
abc
```

### **Output**

```text
2
```

### **Explanation**

Adjacent pairs in `"abc"` are:

* `(a, b)` → `"ab"`
* `(b, c)` → `"bc"`

Distinct adjacent pairs:

```text
{ab, bc}
```

Count = **2**

Now try all possible adjacent swaps:

### Swap positions 0 and 1:

```text
bac
```

Pairs:

* `ba`
* `ac`

Distinct pairs = **2**

### Swap positions 1 and 2:

```text
acb
```

Pairs:

* `ac`
* `cb`

Distinct pairs = **2**

Maximum possible stability = **2**

---

## **Sample Case 2**

### **Input**

```text
abca
```

### **Output**

```text
3
```

### **Explanation**

Original string: `"abca"`

Adjacent pairs:

* `ab`
* `bc`
* `ca`

Distinct pairs:

```text
{ab, bc, ca}
```

Count = **3**

Try all adjacent swaps:

### Swap positions 0 and 1:

```text
baca
```

Pairs:

* `ba`
* `ac`
* `ca`

Distinct = **3**

### Swap positions 1 and 2:

```text
acba
```

Pairs:

* `ac`
* `cb`
* `ba`

Distinct = **3**

### Swap positions 2 and 3:

```text
abac
```

Pairs:

* `ab`
* `ba`
* `ac`

Distinct = **3**

Maximum possible stability = **3**

---

## **Sample Case 3**

### **Input**

```text
aaaa
```

### **Output**

```text
1
```

### **Explanation**

Adjacent pairs:

* `aa`
* `aa`
* `aa`

Distinct adjacent pairs:

```text
{aa}
```

Count = **1**

No matter which adjacent swap is performed, the string remains unchanged.

So the maximum stability score remains **1**.

---

# 🔍 **Key Observation**

When we swap two adjacent characters, **only a few adjacent pairs change**.

For a swap at index `i`, only these positions are affected:

* `(i-1, i)`
* `(i, i+1)`
* `(i+1, i+2)`

All other adjacent pairs remain unchanged.

So instead of recomputing the whole string every time, we can optimize by recalculating only the affected pairs.

---

# 🧠 **Approach 1 (Simple / Brute Force)**

Since:

[
|S| \le 1000
]

A brute-force solution is acceptable.

### Steps:

1. For every possible adjacent swap:

   * Swap `S[i]` and `S[i+1]`
   * Compute all adjacent pairs
   * Count distinct pairs
   * Restore the swap
2. Return the maximum score

---

# ✅ **Brute Force Algorithm**

For each `i` from `0` to `n-2`:

* Swap `s[i]` and `s[i+1]`
* Build all adjacent pairs
* Insert them into a set
* Track maximum size of set
* Undo swap

---

# ⏱️ **Time Complexity**

For each swap:

* counting pairs takes `O(n)`

There are `O(n)` swaps.

So total:

[
O(n^2)
]

With `n <= 1000`, this is perfectly fine.

---

# 💡 **Hint for Students**

### Hint 1

What exactly is a “distinct adjacent pair”?

Example:

```text
abca
```

Pairs are:

```text
ab, bc, ca
```

Distinct count = 3

---

### Hint 2

Try all adjacent swaps manually for a small string like:

```text
abba
```

---

### Hint 3

Use a `Set<String>` to store adjacent pairs.

---

# 🎤 **Interview Discussion Questions**

These are the kind of follow-up questions an interviewer may ask:

### Conceptual

* What is meant by “distinct adjacent pairs”?
* Why do we use a set?
* Why is brute force acceptable here?

### Optimization

* Can you optimize it below `O(n^2)`?
* Which pairs actually change after one adjacent swap?
* Can we avoid recomputing the whole string every time?

### Variations

* What if you were allowed **at most one** swap instead of exactly one?
* What if you could swap **any two characters**, not just adjacent ones?
* What if uppercase letters were also allowed?

---

# 👨‍💻 **Java Solution (Brute Force, Clean & Interview Safe)**

```java
import java.util.*;

public class Main {

    static int getStability(char[] arr) {
        Set<String> set = new HashSet<>();

        for (int i = 0; i < arr.length - 1; i++) {
            String pair = "" + arr[i] + arr[i + 1];
            set.add(pair);
        }

        return set.size();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char[] arr = s.toCharArray();

        int n = arr.length;
        int ans = 0;

        // Try every adjacent swap
        for (int i = 0; i < n - 1; i++) {
            // Swap
            char temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;

            // Compute stability
            ans = Math.max(ans, getStability(arr));

            // Undo swap
            temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }

        System.out.println(ans);
    }
}
```

---

# 🐍 **Python Solution**

```python
def get_stability(s):
    pairs = set()
    for i in range(len(s) - 1):
        pairs.add(s[i] + s[i + 1])
    return len(pairs)

s = list(input().strip())
n = len(s)

ans = 0

for i in range(n - 1):
    s[i], s[i + 1] = s[i + 1], s[i]
    ans = max(ans, get_stability(s))
    s[i], s[i + 1] = s[i + 1], s[i]

print(ans)
```

---

# 🚀 **Optimized Thought (For Strong Students)**

A better optimization idea:

When swapping positions `i` and `i+1`, only these pairs may change:

* `s[i-1]s[i]`
* `s[i]s[i+1]`
* `s[i+1]s[i+2]`

So instead of rebuilding the entire set every time, we can update only local changes.

That gives a more advanced discussion point for interviews.

---

# 📚 **Topics Covered**

This question mainly tests:

* **Strings**
* **Simulation**
* **Brute Force**
* **Set / Hashing**
* **Observation-based optimization**

---

# 🎯 **Closest Platform Practice Questions**

Students should practice similar concepts from:

## **LeetCode**

* Valid Anagram
* Buddy Strings
* Permutation in String
* Count Unique Substrings

## **GeeksforGeeks**

* Distinct substring / pair-based string problems
* Adjacent character manipulation
* String transformation problems

## **Codeforces**

* Constructive string problems
* Swap / adjacency based string questions

---

# 📌 **Best Short Topic Name for Practice Sheet**

You can list this problem under:

```text
Strings + HashSet + Simulation
```

or

```text
String Manipulation + Distinct Pair Counting
```
