

## **Problem Title**

**Make Array Non-Decreasing Using Cyclic Increments**

## **Difficulty Level**

**Easy**

## **Topics**

* Arrays
* Dynamic Programming
* State DP
* Greedy vs DP
* Optimization

## **Problem Description**

You are given an array `arr[]` of size `N`, where each element is a digit from **0 to 9**.

You may perform the following operation any number of times:

* Choose an index `i`
* Increment `arr[i]` by **1**
* If the digit becomes **10**, it wraps around to **0**

Your task is to convert the array into a **non-decreasing array**, meaning:

```text id="i2jff8"
arr[i] ≥ arr[i-1]   for all i > 0
```

Find the **minimum total number of cyclic increments** required.

---

## **Important Rule**

Since the digits are cyclic:

```text id="egxiwg"
9 → 0 → 1 → 2 → ...
```

The cost to convert a digit `a` into digit `b` is:

```text id="e4nyhh"
steps = (b - a + 10) % 10
```

---

## **Example 1**

### **Input**

```text id="az7r79"
N = 5
arr = [1, 3, 2, 1, 1]
```

### **Output**

```text id="jlwm0g"
5
```

### **Explanation**

```text id="mjlwmx"
1 3 2 1 1
→ 1 3 3 1 1   (2 → 3, +1)
→ 1 3 3 3 1   (1 → 3, +2)
→ 1 3 3 3 3   (1 → 3, +2)
```

Total operations = **5**

---

## **Example 2**

### **Input**

```text id="mpck6n"
N = 4
arr = [5, 2, 2, 2]
```

### **Output**

```text id="sr7i3l"
9
```

### **Explanation**

```text id="e5r4yl"
5 2 2 2
→ 5 5 2 2   (+3)
→ 5 5 5 2   (+3)
→ 5 5 5 5   (+3)
```

Total operations = **9**

---

## **Example 3**

### **Input**

```text id="vtceeq"
N = 3
arr = [8, 9, 1]
```

### **Output**

```text id="x61um5"
8
```

### **Explanation**

```text id="z9kmfi"
8 9 1
→ 8 9 9   (1 → 9, +8)
```

Total operations = **8**

---

## **Example 4**

### **Input**

```text id="d9h0vh"
N = 4
arr = [1, 2, 3, 4]
```

### **Output**

```text id="yrx2nl"
0
```

### **Explanation**

Already non-decreasing.

---

## **Constraints**

```text id="8s7mdd"
1 ≤ N ≤ 10^5
0 ≤ arr[i] ≤ 9
```

---

## **Approach Hint**

A direct greedy may fail because cyclic increments can make a **larger digit cheaper or more expensive** depending on wrap-around.

Use **Dynamic Programming**:

* Try making each position end at every digit from `0 to 9`
* Maintain minimum cost while keeping the final sequence non-decreasing

---

## **Expected Complexity**

* **Time:** `O(N × 10 × 10)`
* **Space:** `O(10)`

---

## **Learning Objective**

This problem helps students understand:

* Why greedy is not always safe
* How to model small-state DP
* How cyclic transitions affect optimization decisions

---

## **Similar Problem / Practice Link**

You can map this under similar practice categories:

* Non-decreasing array problems
* DP on digits
* State transition DP
* Cyclic transformation problems

**Suggested platform tags:**

* LeetCode / Codeforces style DP
* Custom Interview DP Practice

---

# **Excel / Sheet Short Row Format**

| Problem Title                                     | Difficulty | Topics               | Core Idea                                                                         | Time Complexity | Similar Link       |
| ------------------------------------------------- | ---------: | -------------------- | --------------------------------------------------------------------------------- | --------------: | ------------------ |
| Make Array Non-Decreasing Using Cyclic Increments |     Easy | Arrays, DP, State DP | Try all final digits 0–9 for each position while maintaining non-decreasing order |      O(N × 100) | Custom DP Practice |

---


