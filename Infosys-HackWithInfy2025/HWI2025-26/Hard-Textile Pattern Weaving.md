
# 🔴 **Q3: Hard — Textile Pattern Weaving**

## 🧩 Problem Statement

You are weaving fabric using threads from two spools:

* Spool A → `A[1..N]`
* Spool B → `B[1..M]`

---

## 📜 Rules

* Use all threads (`N + M`)
* Maintain order of A and B
* At each step:

  * Pick from A or B

---

## 🎨 Scoring

* Same consecutive color → +H
* Different → 0

---

## 🎯 Goal

Maximize total beauty score.

---

## 📥 Input

```
N
M
H
A[]
B[]
```

---

## 📤 Sample Input

```
2
2
5
1 1
1 1
```

## 📤 Output

```
15
```

---

## 💡 Explanation

Sequence: `1 1 1 1`
Pairs:

* (1,1) → +5
* (1,1) → +5
* (1,1) → +5
  Total = 15

---

## 🧠 Approach (2D DP)

### State:

```
dp[i][j][last]
```

But optimize:

```
dp[i][j] = max score using A[0..i], B[0..j]
```

---

## 🔁 Transition

From `(i, j)`:

* Pick A[i]
* Pick B[j]

Check:

* If same as previous → +H

---

## ⚡ Optimized DP Idea

Track last element:

```
dp[i][j] = max(
    dp[i-1][j] + (A[i] == last ? H : 0),
    dp[i][j-1] + (B[j] == last ? H : 0)
)
```

---

## ⏱️ Complexity

* Time: `O(N * M)`
* Space: `O(N * M)`

---

## 💡 Hints

* Think like **merge + LCS**
* Only adjacent matters
* Try greedy grouping same colors

---

## 🎤 Interview Questions

* Can we reduce space to O(M)?
* What if 3 arrays?
* What if reward depends on distance?
* Relation with LCS?

---


