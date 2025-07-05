
# Problem: Maximize the Minimum Game Score

**Marks:** 30
**Negative Marks:** 0

## Problem Description

You are given an array `points` of size `n` and an integer `m`. There is another array `gameScore` of size `n`, where `gameScore[i]` represents the score achieved at the `i`-th game. Initially, `gameScore[i] = 0` for all indices.

You start at index `-1`, which is outside the array (before the first position at index `0`). You can make **at most `m` moves**. In each move, you can either:

* **Increase the index by 1** and add `points[i]` to `gameScore[i]`.
* **Decrease the index by 1** and add `points[i]` to `gameScore[i]`.

> **Important:** The index must always remain within the bounds of the array after the first move (it cannot go outside `0` to `n-1` after the first step).

Your task is to determine the **maximum possible minimum value** in the `gameScore` array after performing at most `m` moves.

---

## Input Format

* The first line contains two integers `n` and `m`:

  * `n`: Size of the `points` array.
  * `m`: Maximum number of allowed moves.
* The second line contains `n` space-separated integers representing the `points` array.

---

## Output Format

* Output a single integer representing the **maximum possible minimum value** in the `gameScore` array after at most `m` moves.

---

## Constraints

* $2 \leq n \leq 5 \times 10^4$
* $1 \leq points[i] \leq 10^6$
* $1 \leq m \leq 10^9$

---

## Example 1

**Input:**

```
2 3
2 4
```

**Output:**

```
4
```

**Explanation:**
Initially, index `i = -1` and `gameScore = [0, 0]`.

| Move | Action     | Index | gameScore |
| ---- | ---------- | ----- | --------- |
| 1    | Increase i | 0     | \[2, 0]   |
| 2    | Increase i | 1     | \[2, 4]   |
| 3    | Decrease i | 0     | \[4, 4]   |

The minimum value in `gameScore` is **4**, and this is the maximum possible minimum among all configurations.

---

## Example 2

**Input:**

```
3 5
1 2 3
```

**Output:**

```
2
```

**Explanation:**
Initially, index `i = -1` and `gameScore = [0, 0, 0]`.

| Move | Action     | Index | gameScore  |
| ---- | ---------- | ----- | ---------- |
| 1    | Increase i | 0     | \[1, 0, 0] |
| 2    | Increase i | 1     | \[1, 2, 0] |
| 3    | Decrease i | 0     | \[2, 2, 0] |
| 4    | Increase i | 1     | \[2, 4, 0] |
| 5    | Increase i | 2     | \[2, 4, 3] |

The minimum value in `gameScore` is **2**, which is the maximum possible minimum achievable.


