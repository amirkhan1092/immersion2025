

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


