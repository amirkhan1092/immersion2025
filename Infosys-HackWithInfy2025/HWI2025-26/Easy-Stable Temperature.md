

## **Problem Title**

**Stable Temperature**

## **Difficulty Level**

**Easy**

## **Topics**

* Arrays
* Greedy
* Simulation
* Right-to-Left Processing

---

## **Problem Description**

You are given an array `T[]` of size `N` representing daily temperatures.

A system is considered **stable** if for every adjacent pair:

```text
|T[i] - T[i-1]| ≤ 1
```

You are allowed to perform the following operation:

* **Decrease any element by 1**
* Each decrease costs **1 operation**
* You can perform this operation **any number of times**

---

## 🎯 **Task**

Find the **minimum number of operations** required to make the array **stable**.

---

## **Input Format**

* First line: Integer `N` (size of array)
* Next `N` lines: Each line contains integer `T[i]`

---

## **Constraints**

```text
1 ≤ N ≤ 10^5
0 ≤ T[i] ≤ 10^9
```

---

## ✅ **Example 1**

### **Input**

```text
N = 4
T = [10, 8, 6, 4]
```

### **Output**

```text
6
```

### **Explanation**

```text
Initial: 10 8 6 4

Step 1: 6 → 5  (since max allowed = 4+1)
Step 2: 8 → 6  (max allowed = 5+1)
Step 3: 10 → 7 (max allowed = 6+1)

Final: 7 6 5 4
Operations = 1 + 2 + 3 = 6
```

---

## ✅ **Example 2**

### **Input**

```text
N = 5
T = [1, 3, 5, 7, 9]
```

### **Output**

```text
10
```

### **Explanation**

```text
1 3 5 7 9
→ 1 2 5 7 9  (+1)
→ 1 2 3 7 9  (+2)
→ 1 2 3 4 9  (+3)
→ 1 2 3 4 5  (+4)

Total = 10
```

---

## ✅ **Example 3**

### **Input**

```text
N = 5
T = [0, 100, 0, 100, 0]
```

### **Output**

```text
198
```

### **Explanation**

```text
0 100 0 100 0

Reduce 100 → 1  (99 ops)
Reduce second 100 → 1 (99 ops)

Final: 0 1 0 1 0
Total = 198
```

---

## 💡 **Approach Hint**

* Since you can **only decrease**, you cannot increase smaller values
* So each element must be **adjusted based on the next element**

👉 Process the array **from right to left**

For each `i`:

```text
T[i] = min(T[i], T[i+1] + 1)
```

Accumulate the difference as operations.

---

## ⚡ **Expected Complexity**

* **Time:** `O(N)`
* **Space:** `O(1)`

---

## 🎯 **Learning Objective**

* Understand greedy adjustment under constraints
* Learn **right-to-left dependency handling**
* Practice minimizing operations with one-directional changes

---

## **Excel / Sheet Row Format**

| Problem Title      | Difficulty | Topics         | Core Idea                                                | Time Complexity | Similar Tag       |
| ------------------ | ---------- | -------------- | -------------------------------------------------------- | --------------- | ----------------- |
| Stable Temperature | Easy       | Arrays, Greedy | Traverse right to left and cap values using next element | O(N)            | Greedy Adjustment |

---


