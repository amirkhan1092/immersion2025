# 🟡 **Q2: Medium — Coffee Shop Rewards**

## 🧩 Problem Statement

A coffee shop runs a reward program for `N` days.

Each day:

* Reward = `R[i]`
* Type:

  * `0` → Regular
  * `1` → Premium

---

## 📜 Rules

### ☕ Regular Reward

* No restriction

### ⭐ Premium Reward

* If taken on day `i`:

  * Cannot take on `i+1` and `i+2`

### ⏭️ Skip

* You can skip any day

---

## 🎯 Goal

Maximize total reward points.

---

## 📥 Input

```
N
R[1..N]
type[1..N]
```

---

## 📤 Sample Input

```
4
10 20 30 40
1 1 1 1
```

## 📤 Output

```
50
```

---

## 💡 Explanation

* Take day 1 (10)
* Skip day 2, 3
* Take day 4 (40)
  → Total = 50

---

## 🧠 Approach (DP)

### Define:

```
dp[i] = max reward from day i to end
```

---

### Transition:

* If regular:

```
dp[i] = max(R[i] + dp[i+1], dp[i+1])
```

* If premium:

```
dp[i] = max(R[i] + dp[i+3], dp[i+1])
```

---

## ⚡ Code Logic

```
for i from N to 1:
    if type[i] == 0:
        dp[i] = max(R[i] + dp[i+1], dp[i+1])
    else:
        dp[i] = max(R[i] + dp[i+3], dp[i+1])
```

---

## ⏱️ Complexity

* Time: `O(N)`
* Space: `O(N)` → can be optimized

---

## 💡 Hints

* This is **House Robber variant**
* Think “take or skip”
* Premium = cooldown problem

---

## 🎤 Interview Questions

* Can you optimize space?
* What if cooldown is dynamic?
* What if multiple premium types?
* Convert to iterative + constant space?
