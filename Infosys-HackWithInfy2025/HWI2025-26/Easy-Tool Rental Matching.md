

# 🟢 **Problem 8 — Tool Rental Matching**

---

## **Difficulty Level**

**Easy**

## **Topics Used**

* Greedy
* Sorting
* Binary Search on Answer
* Two Pointers
* Matching / Assignment Problems

---

# 🧩 Problem Statement

A hardware rental shop has:

* `N` customers requesting tools
* `M` available tools

Each customer `i` needs a tool with at least:

[
P[i]
]

power rating.

Each tool `j` has a base power rating:

[
R[j]
]

---

## **Amplification Option**

You also have:

[
K
]

**power amplifiers** available.

You may choose **up to `K` tools** and attach **one amplifier** to each selected tool.

If a tool with rating `R[j]` is amplified, its effective power becomes:

[
2 \times R[j]
]

### Rules:

* A tool can receive **at most one amplifier**
* A customer can rent **at most one tool**
* Each tool can be rented to **at most one customer**

---

# 🎯 Goal

Find the **maximum number of customers** that can be served.

A customer `i` can be served by tool `j` if:

[
\text{effective power of tool } j \ge P[i]
]

where effective power is either:

* `R[j]` (normal)
* `2 × R[j]` (if amplified)

---

# 📥 Input Format

* The first line contains an integer `N`, denoting the number of customers.
* The second line contains an integer `M`, denoting the number of tools.
* The third line contains an integer `K`, denoting the number of amplifiers.
* The next `N` lines contain one integer each: `P[i]`
* The next `M` lines contain one integer each: `R[j]`

---

# 📌 Constraints

A practical clean version for students:

[
1 \le N, M \le 10^5
]

[
0 \le K \le M
]

[
1 \le P[i], R[j] \le 10^9
]

---

# 📤 Output Format

Print a single integer — the **maximum number of customers** that can be served.

---

# 🧪 Sample Test Cases

---

## **Case 1**

### Input

```text id="v2q8mg"
3
3
1
4
8
5
4
3
6
```

### Output

```text id="rtdx2r"
3
```

### Explanation

Customers need:

```text id="vuj0qu"
[4, 8, 5]
```

Tools available:

```text id="qf2hlv"
[4, 3, 6]
```

Sort them:

* Customers → `[4, 5, 8]`
* Tools → `[3, 4, 6]`

Use amplifier on tool `4`:

[
2 \times 4 = 8
]

Assignments:

* `3` → customer `4` ❌ (cannot)
* Better assignment:

  * `4` → customer `4`
  * `6` → customer `5`
  * amplified `4`/or equivalent match → customer `8`

All 3 can be served optimally.

---

## **Case 2**

### Input

```text id="1fkw8a"
4
3
1
5
6
7
8
3
4
5
```

### Output

```text id="zyeu06"
2
```

### Explanation

Tools:

```text id="x1b6mx"
[3, 4, 5]
```

With one amplifier, we can make one tool double.

Best possible:

* `5` → customer `5`
* amplified `4 → 8` → customer `8`

Total served = **2**

---

## **Case 3**

### Input

```text id="h6c38s"
5
4
2
2
3
6
7
8
1
3
4
5
```

### Output

```text id="v7tupw"
4
```

### Explanation

Best strategy:

* Match smallest customers first
* Use amplifiers only where necessary

This serves **4 customers**.

---

# 💡 Core Idea

This is a **maximize matching** problem.

We want to match:

* customer requirements
  with
* tool powers

while optionally using up to `K` amplifiers.

---

# 🧠 Best Approach

## Step 1

Sort:

* customer requirements
* tool powers

## Step 2

Use **Binary Search on Answer**

We check:

> “Can we serve exactly `x` customers?”

If yes, try larger.
If no, try smaller.

---

# 🔍 Feasibility Check Idea

To check if we can serve `x` customers:

* Take the **smallest `x` customers**
* Try to assign them the **best possible `x` tools**

For each customer:

* first try without amplifier
* if not possible, use amplifier if available

This can be implemented greedily using:

* multiset / TreeMap (Java)
* sorted list / heap (Python alternative)

---

# ✅ Why Greedy Works

Because:

* smaller customers are easier to satisfy
* smaller tools should be used first
* amplifier should be used **only when needed**

This avoids wasting strong tools.

---

# ⏱ Time Complexity

Sorting:

[
O(N \log N + M \log M)
]

Binary Search + Feasibility:

[
O((N + M)\log M \log \min(N, M))
]

Efficient for large inputs.

---

# 👨‍💻 Java Solution

```java id="gs6w4s"
import java.util.*;

public class Main {

    static boolean canServe(int x, int[] customers, int[] tools, int K) {
        if (x == 0) return true;
        if (x > tools.length || x > customers.length) return false;

        TreeMap<Integer, Integer> map = new TreeMap<>();

        // Use the x strongest tools
        for (int i = tools.length - x; i < tools.length; i++) {
            map.put(tools[i], map.getOrDefault(tools[i], 0) + 1);
        }

        int ampsLeft = K;

        // Serve the x hardest customers among the x smallest chosen group
        for (int i = x - 1; i >= 0; i--) {
            int need = customers[i];

            // Try without amplifier
            Integer normal = map.ceilingKey(need);
            if (normal != null) {
                removeOne(map, normal);
                continue;
            }

            // Try with amplifier => need tool >= ceil(need / 2)
            if (ampsLeft > 0) {
                int req = (need + 1) / 2;
                Integer boosted = map.ceilingKey(req);
                if (boosted != null) {
                    removeOne(map, boosted);
                    ampsLeft--;
                    continue;
                }
            }

            return false;
        }

        return true;
    }

    static void removeOne(TreeMap<Integer, Integer> map, int key) {
        int cnt = map.get(key);
        if (cnt == 1) map.remove(key);
        else map.put(key, cnt - 1);
    }

    public static int maxCustomers(int N, int M, int K, int[] P, int[] R) {
        Arrays.sort(P);
        Arrays.sort(R);

        int low = 0, high = Math.min(N, M), ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canServe(mid, P, R, K)) {
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

        int N = Integer.parseInt(sc.nextLine().trim());
        int M = Integer.parseInt(sc.nextLine().trim());
        int K = Integer.parseInt(sc.nextLine().trim());

        int[] P = new int[N];
        int[] R = new int[M];

        for (int i = 0; i < N; i++) P[i] = Integer.parseInt(sc.nextLine().trim());
        for (int i = 0; i < M; i++) R[i] = Integer.parseInt(sc.nextLine().trim());

        System.out.println(maxCustomers(N, M, K, P, R));
    }
}
```

---

# 🐍 Python Solution

```python id="apikyg"
from bisect import bisect_left, insort

def can_serve(x, customers, tools, K):
    if x == 0:
        return True
    if x > len(customers) or x > len(tools):
        return False

    available = sorted(tools[-x:])
    amps_left = K

    for i in range(x - 1, -1, -1):
        need = customers[i]

        # Try normal tool
        idx = bisect_left(available, need)
        if idx < len(available):
            available.pop(idx)
            continue

        # Try amplified tool
        if amps_left > 0:
            req = (need + 1) // 2
            idx = bisect_left(available, req)
            if idx < len(available):
                available.pop(idx)
                amps_left -= 1
                continue

        return False

    return True


def max_customers(N, M, K, P, R):
    P.sort()
    R.sort()

    low, high = 0, min(N, M)
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if can_serve(mid, P[:mid], R, K):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


N = int(input().strip())
M = int(input().strip())
K = int(input().strip())

P = [int(input().strip()) for _ in range(N)]
R = [int(input().strip()) for _ in range(M)]

print(max_customers(N, M, K, P, R))
```

---

# 💭 Hints for Students

### Hint 1

Sort both arrays first.

### Hint 2

Smaller customers should preferably get smaller tools.

### Hint 3

Use amplifier **only when a normal tool is not enough**.

### Hint 4

Try binary search on:

```text id="w7wwt2"
maximum customers served
```

---

# ❌ Common Mistakes

Students often do these mistakes:

* Using amplifier too early
* Giving strongest tools to smallest customers
* Forgetting that each tool can be used only once
* Not sorting before matching
* Greedy without checking feasibility properly

---

# 🎯 Interview Questions Based on This Problem

## Conceptual

* Why is sorting useful here?
* Why does greedy work after sorting?
* Why can we binary search on answer?

## Follow-up Variants

* What if amplifier triples the tool instead of doubling?
* What if each tool can receive multiple amplifiers?
* What if each amplifier has different boost value?
* What if we want to **minimize unused tools**?

## Coding Questions

* Can you solve it without binary search?
* Can you optimize the feasibility check?
* Can you reconstruct which customer got which tool?

---

# 🔗 Similar Practice Links (Active)

## **LeetCode**

* [Assign Cookies](https://leetcode.com/problems/assign-cookies/)
* [Maximum Number of Tasks You Can Assign](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/)
* [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

## **GeeksforGeeks**

* [Assign Cookies / Greedy Matching Type Problems](https://www.geeksforgeeks.org/assign-mice-holes/)
* [Greedy Algorithms Practice](https://www.geeksforgeeks.org/greedy-algorithms/)

## **Codeforces**

* [Greedy Problemset](https://codeforces.com/problemset?tags=greedy)
* [Binary Search + Greedy Problems](https://codeforces.com/problemset?tags=binary%20search,greedy)

---

# 📌 Best Sheet Label

```text id="3pk5oz"
Easy — Greedy Matching with Optional Boost
```

---

