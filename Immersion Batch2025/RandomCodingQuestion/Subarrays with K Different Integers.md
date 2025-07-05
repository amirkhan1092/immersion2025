
# Problem: Subarrays with K Different Integers

**Marks:** 30
**Negative Marks:** 0

---

## Problem Description

You are given an integer array `nums` and an integer `k`. Your task is to **return the number of good subarrays** in `nums`.

A **good subarray** is defined as a contiguous subarray that contains **exactly `k` different integers**.

For example:

* The array `[1, 2, 3, 1, 2]` contains **3 different integers**: 1, 2, and 3.

A **subarray** is a **contiguous part** of an array.

---

## Input Format

* The first line contains an integer `n` – the size of the array.
* The second line contains `n` space-separated integers – the elements of the array `nums`.
* The third line contains an integer `k` – the number of distinct integers required in a subarray.

---

## Output Format

* Output a single integer – the number of subarrays that contain **exactly `k` distinct integers**.

---

## Constraints

* $1 \leq n = nums.length \leq 2 \times 10^4$
* $1 \leq nums[i],\ k \leq n$

---

## Example 1

**Input:**

```
5
1 2 1 2 3
2
```

**Output:**

```
7
```

**Explanation:**
The subarrays with **exactly 2 different integers** are:

* \[1, 2]
* \[2, 1]
* \[1, 2]
* \[2, 3]
* \[1, 2, 1]
* \[2, 1, 2]
* \[1, 2, 1, 2]

Total good subarrays = **7**

---

## Example 2

**Input:**

```
5
1 2 1 3 4
3
```

**Output:**

```
3
```

**Explanation:**
The subarrays with **exactly 3 different integers** are:

* \[1, 2, 1, 3]
* \[2, 1, 3]
* \[1, 3, 4]

Total good subarrays = **3**

