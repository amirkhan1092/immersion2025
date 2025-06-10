

## 🧠 **Scenario**

Walmart Labs has a unique seating optimization problem. In their tech campus, people often sit scattered across a row of chairs. For better team collaboration, people need to sit together without any gaps. However, to avoid too much walking, they aim to minimize the total movement cost. Can you write a program that solves this efficiently?

---

## 📌 **Problem Statement**

You are given a list of `N` seats in a row, where each seat is represented as either:

* `0`: empty seat
* `1`: seat occupied by a person

There are exactly `M` people sitting (`M < N`). Your task is to move people such that they occupy `M` consecutive seats (i.e., no gaps), and the **total cost** (defined as the **sum of absolute distances** each person moves) is **minimized**.

You may only move people (1s), and they can be placed into any empty seats (0s), but the final configuration should have all the 1s adjacent to each other.

---

## 🧮 **Input Format**

* An integer `N` – total number of seats (1 ≤ N ≤ 10⁵)
* A list of `N` integers – each element is either 0 or 1

---

## 📤 **Output Format**

* A single integer – the minimum total movement cost required to eliminate all gaps

---

## 🧪 **Sample Input**

```
9  
0 1 1 0 1 0 0 0 1
```

---

## ✅ **Sample Output**

```
5
```

---

## 🔍 **Explanation**

Initial:
`[0, 1, 1, 0, 1, 0, 0, 0, 1]`

Positions of people: `[1, 2, 4, 8]`
If we move them to occupy positions `[3, 4, 5, 6]`, the cost is:

```
|1-3| + |2-4| + |4-5| + |8-6| = 2 + 2 + 1 + 2 = 7
```

But if we shift them to `[2, 3, 4, 5]`, the cost is:

```
|1-2| + |2-3| + |4-4| + |8-5| = 1 + 1 + 0 + 3 = 5
```

This is the **minimum total cost**.

---

## 🧠 **Constraints**

* `1 ≤ N ≤ 10⁵`
* Seats array contains only 0s and 1s
* Number of 1s (`M`) is at least 1 and strictly less than `N`

---

## 🧠 **Approach Hint**

* Extract the indices of people (1s)
* Use a **median-based alignment** to reduce the total movement
* Calculate the cost to shift each person to a set of consecutive seats around the median

---

## 🧪 **Test Cases**

### ✅ Test Case 1

**Input:**

```
5  
1 0 0 0 1
```

**Output:**

```
3
```

### ✅ Test Case 2

**Input:**

```
7  
0 0 1 0 0 1 0
```

**Output:**

```
2
```

### ✅ Test Case 3

**Input:**

```
6  
1 0 1 0 0 0
```

**Output:**

```
1
```

### ✅ Test Case 4

**Input:**

```
9  
0 0 0 1 1 1 0 0 0
```

**Output:**

```
0
```

### ✅ Test Case 5

**Input:**

```
10  
1 0 0 1 0 0 0 1 0 1
```

**Output:**

```
8
```


