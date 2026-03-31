

## *Focus: OA + Interview Preparation*

---

# 🟢 1) **String Stability Boost**

### **Difficulty:** Easy

### **Topics:**

`Strings`, `HashSet`, `Simulation`, `Adjacent Swap`

---

## 🧩 **Problem Description**

You are given a string `S` of lowercase letters.

The **stability score** is the number of **distinct adjacent pairs** `(S[i], S[i+1])`.

You must perform **exactly one adjacent swap** and maximize the stability score.

---

## 🧪 **Example**

**Input**

```
abc
```

**Output**

```
2
```

---

## 💡 **Approach**

* Try all adjacent swaps
* Count distinct pairs using `Set`
* Track maximum

⏱ Complexity: `O(N^2)`

---

## 🎯 **Interview Focus**

* String manipulation
* Set usage
* Local change observation

---

## 🔗 **Similar Practice**

* [https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
* [https://www.geeksforgeeks.org/count-distinct-substrings-string/](https://www.geeksforgeeks.org/count-distinct-substrings-string/)

---

---

# 🟢 2) **Blocks**

### **Difficulty:** Easy

### **Topics:**

`Greedy`, `Sorting`, `Binary Construction`, `Math`

---

## 🧩 **Problem Description**

You are given:

* Array `A` → sizes of 1-blocks
* Array `B` → sizes of 0-blocks

You must:

* Use all blocks exactly once
* Arrange them alternately (0,1 or 1,0)
* Form a binary string

Maximize its **decimal value (mod 1e9+7)**.

---

## 🧪 **Example**

**Input**

```
1
2
1
```

**Output**

```
6
```

---

## 💡 **Approach**

* Greedy: place larger 1-blocks earlier
* Binary value → leftmost importance
* Efficient modular computation

---

## 🎯 **Interview Focus**

* Greedy logic
* Binary number formation
* Optimization thinking

---

## 🔗 **Similar Practice**

* [https://leetcode.com/problems/largest-number/](https://leetcode.com/problems/largest-number/)
* [https://codeforces.com/problemset?tags=greedy](https://codeforces.com/problemset?tags=greedy)

---

---

# 🟡 3) **Recamán Queries**

### **Difficulty:** Medium

### **Topics:**

`Segment Tree`, `Range Query`, `Math`, `Precomputation`

---

## 🧩 **Problem Description**

Given array `A` and queries:

### Query Types:

* `0 i x` → Update A[i] = x
* `1 L R` →

  * Find max `M` in range
  * Compute **Recamán distance**
  * Multiply by 17 if M is “fortunate”

Return **sum of all query results**.

---

## 🧪 **Example**

**Output**

```
2472
```

---

## 💡 **Approach**

* Use **Segment Tree** for max queries
* Precompute:

  * Recamán steps
  * Fortunate numbers
* Answer queries efficiently

⏱ Complexity: `O((N+Q) log N)`

---

## 🎯 **Interview Focus**

* Segment Tree implementation
* Precomputation optimization
* Handling mixed queries

---

## 🔗 **Similar Practice**

* [https://leetcode.com/problems/range-sum-query-mutable/](https://leetcode.com/problems/range-sum-query-mutable/)
* [https://www.geeksforgeeks.org/segment-tree-set-2-range-maximum-query-node-update/](https://www.geeksforgeeks.org/segment-tree-set-2-range-maximum-query-node-update/)

---

---

# 🔴 4) **Terrain Color Trail**

### **Difficulty:** Hard

### **Topics:**

`2D DP`, `Grid`, `Path Optimization`, `State Transition`

---

## 🧩 **Problem Description**

You are given:

* Grid `V[i][j]` → value
* Grid `Color[i][j]` → terrain color
* Bonus `B`

You can move:

* Right or Down

Score:

* Add `V[i][j]`
* If same color as previous cell → +B

Find **maximum total score from (0,0) to (N-1,M-1)**.

---

## 🧪 **Example**

**Output**

```
35
```

---

## 💡 **Approach**

* Use **DP[i][j]**
* Transition:

  * From top
  * From left
* Add bonus if colors match

⏱ Complexity: `O(N*M)`

---

## 🎯 **Interview Focus**

* 2D DP design
* Transition logic
* Edge cases

---

## 🔗 **Similar Practice**

* [https://leetcode.com/problems/maximum-path-sum/](https://leetcode.com/problems/maximum-path-sum/)
* [https://leetcode.com/problems/minimum-path-sum/](https://leetcode.com/problems/minimum-path-sum/)
* [https://www.geeksforgeeks.org/dynamic-programming-grid-problems/](https://www.geeksforgeeks.org/dynamic-programming-grid-problems/)

---

---

# 🔴 5) **Film Festival Program**

### **Difficulty:** Hard

### **Topics:**

`DP`, `Greedy`, `Sorting`, `State DP`, `Optimization`

---

## 🧩 **Problem Description**

You have:

* `N` films with:

  * Genre `G[i]`
  * Value `A[i]`
* Select exactly `D` films

Constraint:

* If consecutive films have same genre → penalty `P`

Maximize:

```
Total Score = Sum(A[i]) - penalties
```

---

## 🧪 **Example**

**Input**

```
4
4
3
5
```

**Output**

```
75
```

---

## 💡 **Approach**

* Sort films by value
* Use **DP or greedy with tracking last genre**
* Balance:

  * High value vs penalty

---

## 🎯 **Interview Focus**

* DP with state (last genre)
* Greedy vs DP trade-off
* Optimization reasoning

---

## 🔗 **Similar Practice**

* [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* [https://codeforces.com/problemset?tags=dp](https://codeforces.com/problemset?tags=dp)

---

---

# 📌 **Final Instruction for Students**

👉 Prepare ALL questions with:

* Dry run
* Brute force + optimized approach
* Time & space complexity
* Edge cases

⚠ Be ready to explain in interview style.






---

# **DSA / Coding Practice Sheet (Consolidated)**

## **1) Lazy Student**

### **Difficulty**

**Easy**

### **Topics**

* Greedy
* Math / Expected Value
* Sorting

### **Problem Description**

You are given a test with `n` questions, each worth `x[i]` marks, a passing threshold `m`, and `c` answer choices per question.

For each question, you may either:

* **Think and answer correctly** → get full marks
* **Guess randomly** → expected marks = `x[i] / c`

You want to **minimize the number of questions you actually think through**, while ensuring the **expected total score is at least `m`**.

Find the **minimum number of questions** you must think through.

### **Core Idea**

Start with expected score if all are guessed, then choose the questions with maximum extra gain:

```text
gain = x[i] - x[i]/c
```

Pick the largest gains first.

### **Expected Complexity**

* Time: `O(N log N)`
* Space: `O(N)`

---

## **2) Tool Rental Matching**

### **Difficulty**

**Easy**

### **Topics**

* Greedy
* Sorting
* Binary Search / Two Pointers

### **Problem Description**

A hardware rental shop has:

* `N` customers, each requiring minimum tool power `P[i]`
* `M` tools, each with base power `R[j]`

You also have `K` power amplifiers.
If a tool is amplified, its power becomes:

```text
2 × R[j]
```

Each tool can be used for at most one customer, and each customer can rent at most one tool.

Find the **maximum number of customers** that can be served.

### **Core Idea**

* Sort customer requirements and tool powers
* Try assigning tools greedily
* Use amplifier only when necessary

### **Expected Complexity**

* Time: `O((N+M) log (N+M))`
* Space: `O(1)` / `O(N)`

---

## **3) Stable Temperature**

### **Difficulty**

**Easy**

### **Topics**

* Arrays
* Greedy
* Simulation

### **Problem Description**

You are given an array `T[]` of size `N` representing daily temperatures.

A system is considered **stable** if:

```text
|T[i] - T[i-1]| ≤ 1
```

You may **decrease any element** any number of times.
Each decrease by `1` costs `1 operation`.

Find the **minimum total operations** required to make the array stable.

### **Example**

```text
Input:
N = 4
T = [10, 8, 6, 4]

Output:
6
```

### **Core Idea**

Process from **right to left**:

```text
T[i] = min(T[i], T[i+1] + 1)
```

### **Expected Complexity**

* Time: `O(N)`
* Space: `O(1)`

---

## **4) Make Array Non-Decreasing Using Cyclic Increments**

### **Difficulty**

**Medium**

### **Topics**

* Arrays
* Dynamic Programming
* State DP

### **Problem Description**

You are given an array `arr[]` of size `N`, where each element is a digit from `0 to 9`.

Operation allowed:

* Increment any `arr[i]` by `1`
* If it becomes `10`, it wraps to `0`

Goal: make the array **non-decreasing** using minimum operations.

### **Important Rule**

```text
steps(a → b) = (b - a + 10) % 10
```

### **Core Idea**

For each position, try all final digits `0..9` and use DP to maintain minimum cost while keeping the sequence non-decreasing.

### **Expected Complexity**

* Time: `O(N × 10 × 10)`
* Space: `O(10)`

---

## **5) Minimum Cost Product Jump**

### **Difficulty**

**Medium**

### **Topics**

* Dynamic Programming
* Arrays
* Sliding Window / Optimization

### **Problem Description**

You are given:

* Array `A` of size `N`
* Integer `K`

You start at index `0` and must reach index `N-1`.

From index `i`, you may jump to any `j` such that:

```text
i < j ≤ i + K
```

Cost of jump:

```text
A[i] × A[j]
```

Find the **minimum total cost** to reach the last index.

### **Core Idea**

Use DP:

```text
dp[i] = min(dp[j] + A[j]*A[i]) for valid j
```

### **Expected Complexity**

* Basic DP: `O(NK)`
* Optimized possible depending on constraints

---

## **6) Dual Timeline Tasks**

### **Difficulty**

**Medium**

### **Topics**

* Dynamic Programming
* Scheduling
* Prefix DP

### **Problem Description**

There are `N` repair tasks in fixed order.

Each task `i` has:

* `D[i]` → time required
* `P[i]` → penalty weight

Two teams (**A** and **B**) work in parallel.

Rules:

* Tasks must be processed in given order
* Each task assigned to exactly one team
* Each team processes its assigned tasks sequentially
* If a task finishes at time `T`, penalty =

```text
T × P[i]
```

Find the **minimum total penalty**.

### **Core Idea**

DP on task assignment and cumulative completion times.

### **Expected Complexity**

* DP based
* State compression may be needed

---

## **7) Emil’s Special Longest Common Sequence**

### **Difficulty**

**Medium**

### **Topics**

* Dynamic Programming
* Strings
* LCS Variation

### **Problem Description**

Given two strings `A` and `B`.

A common subsequence has score:

```text
Score = (Length of subsequence) × (Number of occurrences of 'e')
```

Find the **maximum possible score** among all common subsequences.

### **Core Idea**

Modified LCS DP keeping track of:

* subsequence length
* count of `'e'`

### **Expected Complexity**

* Time: `O(N × M × state)`
* Space: depends on optimization

---

## **8) Mosaic Tile Optimization**

### **Difficulty**

**Medium**

### **Topics**

* Dynamic Programming
* Grid DP
* Bitmask DP

### **Problem Description**

You are tiling an `N × M` wall.

Available tiles:

* **Type A** → `1 × 1`, cost = `costA`
* **Type B** → `1 × 2` horizontal, cost = `costB`

Some cells are marked as **accent cells** with beauty bonus `V[i][j]`.

Rules:

* If an accent cell is covered by **Type A**, bonus is earned
* If covered by **Type B**, no bonus

Net cost:

```text
Net Cost = Total tile cost - Total beauty bonus
```

Find the **minimum net cost**.

### **Core Idea**

Row-by-row DP / bitmask transitions for tiling.

### **Expected Complexity**

* Usually DP on rows / states

---

## **9) Balanced Palindrome Partitioning**

### **Difficulty**

**Hard**

### **Topics**

* Strings
* DP
* Binary Search on Answer
* Palindrome DP

### **Problem Description**

Given:

* String `S` of length `N`
* Integer `K`

Partition the entire string into contiguous substrings such that **at least `K` substrings are palindromes**.

Among all valid partitions, maximize:

```text
length of the shortest substring
```

Return that maximum possible value.

### **Core Idea**

* Binary search on minimum allowed substring length
* DP to check whether at least `K` palindrome parts are possible

### **Expected Complexity**

* Palindrome preprocessing + DP

---

## **10) Spice Blend Sequencing**

### **Difficulty**

**Hard**

### **Topics**

* Dynamic Programming
* Sequence Merging
* 3D DP

### **Problem Description**

A chef combines spices from two collections:

* Collection `A` has `N` spices
* Collection `B` has `M` spices

Need to select exactly `K` spices in total.

Rules:

* Pick only from the **front** of either collection
* Relative order inside each collection must remain preserved

Each spice has:

* flavor profile
* intensity value

Score consists of:

1. **Intensity sum**
2. **Harmony bonus `H`** if two consecutive chosen spices have same flavor

Find the **maximum total score**.

### **Core Idea**

DP on:

* how many taken from A
* how many taken from B
* how many selected
* last flavor/source

### **Expected Complexity**

* Multi-dimensional DP

---

# **Excel / Tracker Friendly Summary Table**

| S.No. |                                     Problem Title | Difficulty | Topics                     | Core Idea                       | Time Complexity   |
| ----- | ------------------------------------------------: | ---------- | -------------------------- | ------------------------------- | ----------------- |
| 1     |                                      Lazy Student | Easy       | Greedy, Expected Value     | Pick max gain questions first   | O(N log N)        |
| 2     |                              Tool Rental Matching | Easy       | Greedy, Sorting            | Match customers/tools optimally | O((N+M) log(N+M)) |
| 3     |                                Stable Temperature | Easy       | Arrays, Greedy             | Right-to-left reduction         | O(N)              |
| 4     | Make Array Non-Decreasing Using Cyclic Increments | Medium     | DP, Arrays                 | Digit-state DP                  | O(N × 100)        |
| 5     |                         Minimum Cost Product Jump | Medium     | DP, Arrays                 | Jump DP                         | O(NK)             |
| 6     |                               Dual Timeline Tasks | Medium     | DP, Scheduling             | Assign tasks to 2 teams         | DP-based          |
| 7     |            Emil’s Special Longest Common Sequence | Medium     | Strings, DP                | Modified LCS                    | O(NM) approx      |
| 8     |                          Mosaic Tile Optimization | Medium     | Grid DP, Bitmask           | Tile placement optimization     | State DP          |
| 9     |                  Balanced Palindrome Partitioning | Hard       | Strings, DP, Binary Search | Maximize shortest valid part    | Advanced DP       |
| 10    |                            Spice Blend Sequencing | Hard       | DP, Sequence Merge         | Multi-state merge DP            | Advanced DP       |

---

# **Recommended Sheet Columns**

If you’re maintaining student practice tracking, use:

```text
Problem Title | Difficulty | Topics | Date Uploaded | Solved By | Practice Link | Status | Notes
```

---


