

# 🟢 **Q1: Easy — Warehouse Crate Loading**

## 🧩 Problem Statement

A warehouse needs to load `N` crates onto `M` pallets.

* Each crate has weight `W[i]`
* Each pallet has capacity `K[j]`

Before loading, each crate must be placed in a bag.

### 🎒 Bag Rules

If you load `k` crates:

* You must use exactly `k` bags
* Bag weights:
  `0, 1, 2, ..., k-1`

Each crate is assigned exactly one bag.

---

## ⚠️ Constraints

* Each pallet holds **only one crate**
* A crate can be placed only if:

[
W[i] + bag \le K[j]
]

---

## 🎯 Goal

Find the **maximum number of crates** that can be loaded.

---

## 📥 Input Format

```
N
M
W1 W2 ... WN
K1 K2 ... KM
```

---

## 📤 Sample Input

```
2
2
9 9
10 10
```

## 📤 Output

```
2
```

---

## 💡 Explanation

* Use bags: 0, 1
* Assign:

  * 9 + 0 → 9 ≤ 10 ✅
  * 9 + 1 → 10 ≤ 10 ✅

---

## 🧠 Approach

### Key Idea:

* Smaller crates + smaller bags
* Larger pallets for heavier combinations

### Steps:

1. Sort crates
2. Sort pallets
3. Binary search on `k`
4. Check if `k` crates can be assigned

---

## ⚡ Efficient Solution (Greedy + Binary Search)

### Pseudocode:

```
sort(W)
sort(K)

low = 0, high = min(N, M)

while low <= high:
    mid = (low + high) / 2
    if possible(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
```

---

## ⏱️ Complexity

* Sorting: `O(N log N)`
* Check: `O(N)`
* Overall: `O(N log N)`

---

## 💡 Hints

* Always try smallest crates first
* Assign largest pallet to hardest case
* Think “matching problem”

---

## 🎤 Interview Questions

* Why binary search?
* Can this be solved using heap?
* What if bags had random weights?
* Variation: multiple crates per pallet?

---


