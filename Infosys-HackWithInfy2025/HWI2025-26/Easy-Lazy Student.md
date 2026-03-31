

# 🟢 **Problem — Lazy Student**

---

## **Difficulty Level**

**Easy**

## **Topics Used**

* Greedy
* Expected Value
* Sorting
* Prefix / Accumulation Thinking
* Optimization

---

# 🧩 Problem Statement

You are given a test with:

* `n` questions
* each question is worth `x[i]` marks
* passing threshold = `m` marks

For each question, you have **two options**:

### 1) Think and answer correctly

If you think and answer the question, you get:

[
x[i]
]

marks with certainty.

### 2) Guess randomly

Each question has exactly `c` options, and only one is correct.

So if you guess randomly, the **expected marks** from that question are:

[
\frac{x[i]}{c}
]

---

## 🎯 Goal

You are a **lazy student** and want to **minimize the number of questions you actually think through**, while still ensuring that your **expected total score is at least `m`**.

Find the **minimum number of questions** you must think through.

---

# 📥 Input Format

* The first line contains an integer `n`, denoting the number of questions.
* The second line contains an integer `m`, denoting the passing threshold.
* The third line contains an integer `c`, denoting the number of choices in each question.
* The next `n` lines each contain an integer `x[i]`, the marks of the `i-th` question.

---

# 📌 Constraints

From the screenshot, the intended constraints are:

[
1 \le n \le 10^5
]

[
1 \le m \le 10^9
]

[
1 \le c \le 10^9
]

[
1 \le x[i] \le 10^9
]

---

# 📤 Output Format

Print a single integer — the **minimum number of questions** you need to think through.

If even after thinking all questions the expected score is still less than `m`, print:

```text id="4c9i0j"
-1
```

---

# 🧪 Sample Test Cases

---

## **Case 1**

### Input

```text id="ofpsqg"
1
1
2
1
```

### Output

```text id="fx36ja"
1
```

### Explanation

There is only one question worth `1` mark.

If guessed randomly:

[
\frac{1}{2} = 0.5
]

Expected score is less than passing threshold `1`.

So you must **think through that question**.

Answer = **1**

---

## **Case 2**

### Input

```text id="w7ctk6"
2
15
2
7
8
```

### Output

```text id="gxt0df"
2
```

### Explanation

Questions are worth:

```text id="6ssig3"
[7, 8]
```

If guessed randomly, expected score:

[
\frac{7}{2} + \frac{8}{2} = 3.5 + 4 = 7.5
]

Not enough.

If you think through only the `8` mark question:

Expected score becomes:

[
8 + \frac{7}{2} = 11.5
]

Still not enough.

If you think through both:

[
7 + 8 = 15
]

This meets the passing threshold.

Answer = **2**

---

## **Case 3**

### Input

```text id="e3p4gm"
3
1
3
1
1
1
```

### Output

```text id="d53q7f"
0
```

### Explanation

If all are guessed randomly:

[
\frac{1}{3} + \frac{1}{3} + \frac{1}{3} = 1
]

Expected score already reaches the passing threshold.

So no need to think through any question.

Answer = **0**

---

# 💡 Key Observation

For every question:

* If you **guess**, expected marks =
  [
  \frac{x[i]}{c}
  ]

* If you **think**, marks =
  [
  x[i]
  ]

So the **extra gain** from thinking instead of guessing is:

[
x[i] - \frac{x[i]}{c} = x[i]\left(1 - \frac{1}{c}\right)
]

This means:

> To maximize score increase with minimum number of questions,
> you should think through the **highest-mark questions first**.

---

# 🧠 Best Approach

## Step 1

Assume you guess **all** questions first.

Initial expected score:

[
\sum \frac{x[i]}{c}
]

## Step 2

If this is already ≥ `m`, answer is `0`.

## Step 3

Otherwise, sort `x[i]` in **descending order**.

## Step 4

Keep converting guessed questions into “thought” questions one by one from largest marks first.

As soon as expected score becomes at least `m`, stop.

That count is your answer.

---

# ✅ Why Greedy Works

Each time you decide to “think” a question instead of guessing, the increase in expected score is proportional to `x[i]`.

So to minimize the number of questions:

* always choose the **largest marks first**

This is a classic **greedy optimization**.

---

# ⏱ Time Complexity

Sorting takes:

[
O(n \log n)
]

Everything else is linear:

[
O(n)
]

Total:

[
O(n \log n)
]

---

# 👨‍💻 Java Solution

```java id="vskpku"
import java.util.*;

public class Main {
    public static int minQuestionsToThink(int n, long m, long c, long[] x) {
        double expected = 0.0;

        for (long val : x) {
            expected += (double) val / c;
        }

        if (expected >= m) return 0;

        Arrays.sort(x); // ascending

        int count = 0;

        for (int i = n - 1; i >= 0; i--) {
            expected += x[i] - (double) x[i] / c;
            count++;

            if (expected >= m) return count;
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine().trim());
        long m = Long.parseLong(sc.nextLine().trim());
        long c = Long.parseLong(sc.nextLine().trim());

        long[] x = new long[n];
        for (int i = 0; i < n; i++) {
            x[i] = Long.parseLong(sc.nextLine().trim());
        }

        System.out.println(minQuestionsToThink(n, m, c, x));
    }
}
```

---

# 🐍 Python Solution

```python id="w4g95b"
def min_questions_to_think(n, m, c, x):
    expected = sum(val / c for val in x)

    if expected >= m:
        return 0

    x.sort(reverse=True)

    count = 0
    for val in x:
        expected += val - (val / c)
        count += 1
        if expected >= m:
            return count

    return -1


n = int(input().strip())
m = int(input().strip())
c = int(input().strip())

x = [int(input().strip()) for _ in range(n)]

print(min_questions_to_think(n, m, c, x))
```

---

# 💭 Hints for Students

### Hint 1

Start by assuming you guess **everything**.

### Hint 2

What is the expected score for one guessed question?

### Hint 3

If you “upgrade” a guessed question into a solved question, how much score increases?

### Hint 4

Which questions should be upgraded first?

---

# ❌ Common Mistakes

Students may make these mistakes:

* Trying DP unnecessarily
* Not using expected value properly
* Sorting in ascending order instead of descending
* Forgetting that guessed questions still contribute some expected score
* Using integer division instead of floating-point logic

---

# 🎯 Interview Questions Based on This Problem

## Conceptual

* Why is expected value enough here?
* Why does greedy work?
* Why choose highest marks first?

## Follow-up Variants

* What if each question has different number of options `c[i]`?
* What if wrong answers have negative marking?
* What if guessing is not uniform random?
* What if you want **minimum time spent**, not minimum number of questions?

## Coding Variants

* Can you solve it without floating point?
* Can you solve it using fractions / integer math safely?
* Can you also print **which questions** to think through?

---

# 🔗 Similar Practice Links (Active)

## **LeetCode**

* [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)
* [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)
* [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## **GeeksforGeeks**

* [Expected Value Basics](https://www.geeksforgeeks.org/expected-value/)
* [Greedy Algorithms](https://www.geeksforgeeks.org/greedy-algorithms/)

## **Codeforces**

* [Greedy Problemset](https://codeforces.com/problemset?tags=greedy)
* [Sorting Problemset](https://codeforces.com/problemset?tags=sortings)

---

# 📌 Best Sheet Label

```text id="hh3oig"
Easy — Greedy Optimization using Expected Value
```

---

## 📝 One-Line Student Understanding

> “Start with all guessed questions, then greedily convert the highest-mark questions into sure-shot answers until expected score reaches the target.”

---

