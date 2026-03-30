
# **Problem: Film Festival Program**

## **Problem Statement**

You are organizing a prestigious film festival that runs for exactly `D` days.

There are `N` films available to choose from.
Each film `i`:

* belongs to a genre `G[i]`, where `1 <= G[i] <= K`
* has an audience appeal score `A[i]`

You must schedule **exactly one film per day** for `D` days, subject to the following rules:

* Each film can be screened **at most once**
* The audience prefers **variety** in the festival schedule
* If the film screened on day `d` has the **same genre** as the film screened on day `d-1`, a fixed **repetition penalty `P`** is applied
* If the genres are different, **no penalty** is applied

---

## **Festival Score**

The total festival score is defined as:

[
\text{Score} = \left(\sum \text{appeal scores of selected films}\right) - \left(\text{total repetition penalties}\right)
]

Your task is to find the **maximum possible total score** by selecting and ordering the films optimally.

---

# **Input Format**

* The first line contains an integer `N` — the total number of available films.
* The second line contains an integer `D` — the total number of festival days.
* The third line contains an integer `K` — the total number of possible genres.
* The fourth line contains an integer `P` — the penalty for screening films of the same genre on consecutive days.
* The next `N` lines each contain **2 space-separated integers**:

  * `G[i]` — the genre of the `i-th` film
  * `A[i]` — the audience appeal score of the `i-th` film

---

# **Output Format**

Print a single integer — the **maximum possible total festival score**.

---

# **Constraints**

* `D <= N <= 5000`
* `1 <= D <= 1000`
* `1 <= K <= 100`
* `1 <= P <= 10^5`
* `1 <= G[i] <= K`
* `1 <= A[i] <= 10^5`

---

# **Sample Test Cases**

---

## **Example 1**

### **Input**

```text id="s1gk0f"
2
2
1
50
1 100
1 100
```

### **Output**

```text id="g0o3za"
150
```

### **Explanation**

There are only 2 films, both of the same genre.

Optimal schedule:

```text id="7s5r2b"
Day 1 → Film 1 (Genre 1, Appeal 100)
Day 2 → Film 2 (Genre 1, Appeal 100)
```

Total appeal:

```text id="z6b6x9"
100 + 100 = 200
```

Penalty:

```text id="yocx2k"
50
```

Final score:

```text id="7vv0fi"
200 - 50 = 150
```

---

## **Example 2**

### **Input**

```text id="6vbe2d"
4
4
3
5
1 10
2 10
3 30
1 15
```

### **Output**

```text id="2x7tr6"
60
```

### **Explanation**

A best ordering is:

```text id="f08q7m"
(Genre 1, 15) → (Genre 3, 30) → (Genre 2, 10) → (Genre 1, 10)
```

Total appeal:

```text id="5v0hs4"
15 + 30 + 10 + 10 = 65
```

Since no two consecutive films have the same genre, penalty = `0`.

Final score:

```text id="iqv4dl"
65
```

> **Important correction:**
> The output should logically be **65**, not **75**.
> Based on the given input, **75 is impossible**.

---

## **Example 3**

### **Corrected Input**

Your sample 3 was missing `K`.
A corrected valid version is:

```text id="c4zcdy"
4
3
2
10
1 50
1 40
2 100
2 80
```

### **Output**

```text id="k2qjlwm"
230
```

### **Explanation**

Choose the best 3 films and arrange them optimally.

Best schedule:

```text id="0f55gm"
(Genre 2, 100) → (Genre 1, 50) → (Genre 2, 80)
```

Total appeal:

```text id="mqn5fw"
100 + 50 + 80 = 230
```

Genres alternate, so penalty = `0`.

Final score:

```text id="xldmrq"
230
```

---

# **Key Insight**

This is **not just “pick top D appeal values”**.

Because:

* the **order matters**
* the **genre sequence matters**
* consecutive same genres reduce score

So the problem is a combination of:

* **selection**
* **ordering**
* **dynamic programming**
* **top values by category**

---

# **Observation**

Suppose you group all films by genre.

For each genre:

* Sort films by appeal in **descending order**
* If you decide to take `x` films from a genre, you will obviously take the **top `x` appeal values**

So the problem becomes:

## Reformulated Problem

Choose how many films to take from each genre, such that:

* total selected films = `D`
* total appeal is maximized
* while arranging genres to minimize / manage same-genre adjacency penalty

---

# **Why This Is Hard**

Because even after choosing the films, you still need to decide:

* Can the selected films be arranged so that same genres do **not** touch?
* If not, how many unavoidable adjacent same-genre pairs will exist?

This becomes a **counting + arrangement optimization** problem.

---

# **Important Arrangement Fact**

If among selected films, the maximum count of any one genre is `mx`, and total selected films are `D`:

Then the **minimum possible number of same-genre adjacent penalties** is:

[
\max(0, 2 \cdot mx - D - 1)
]

This comes from the standard **rearrangement / spacing** logic.

So once you know how many films are selected from each genre:

* Total appeal = sum of selected values
* Penalty count = minimum unavoidable adjacent equal-genre pairs
* Total score = appeal − penalty count × `P`

---

# **Efficient Strategy**

## Step 1

Group films by genre.

## Step 2

Sort each genre’s appeal list in descending order.

## Step 3

Build prefix sums for each genre:

* `prefix[g][x]` = sum of top `x` films of genre `g`

## Step 4

Use DP to decide how many films to take from each genre.

State idea:

[
dp[g][used][mx]
]

where:

* `g` = processed genres
* `used` = number of selected films so far
* `mx` = maximum selected count among any genre so far

This lets us later compute:

[
\text{penaltyPairs} = \max(0, 2 \cdot mx - D - 1)
]

Then:

[
\text{answer} = \max(\text{appealSum} - \text{penaltyPairs} \cdot P)
]

---

# **Complexity**

Since:

* `K <= 100`
* `D <= 1000`

A DP of roughly:

[
O(K \cdot D^2)
]

is feasible.

---

# **Java Solution (Optimized DP)**

```java id="m5m5j4"
import java.util.*;

public class Solution {
    public static long solve(int N, int D, int K, int P, int[][] films) {
        List<Integer>[] genreFilms = new ArrayList[K + 1];
        for (int i = 1; i <= K; i++) genreFilms[i] = new ArrayList<>();

        for (int[] film : films) {
            int g = film[0];
            int a = film[1];
            genreFilms[g].add(a);
        }

        // Sort each genre descending
        for (int g = 1; g <= K; g++) {
            genreFilms[g].sort(Collections.reverseOrder());
        }

        // Prefix sums
        long[][] prefix = new long[K + 1][D + 1];
        for (int g = 1; g <= K; g++) {
            int sz = genreFilms[g].size();
            for (int i = 1; i <= Math.min(D, sz); i++) {
                prefix[g][i] = prefix[g][i - 1] + genreFilms[g].get(i - 1);
            }
        }

        // dp[used][mx] = max appeal sum
        long[][] dp = new long[D + 1][D + 1];
        for (int i = 0; i <= D; i++) Arrays.fill(dp[i], Long.MIN_VALUE / 4);
        dp[0][0] = 0;

        for (int g = 1; g <= K; g++) {
            long[][] ndp = new long[D + 1][D + 1];
            for (int i = 0; i <= D; i++) Arrays.fill(ndp[i], Long.MIN_VALUE / 4);

            int sz = Math.min(D, genreFilms[g].size());

            for (int used = 0; used <= D; used++) {
                for (int mx = 0; mx <= D; mx++) {
                    if (dp[used][mx] <= Long.MIN_VALUE / 8) continue;

                    for (int take = 0; take + used <= D && take <= sz; take++) {
                        int newUsed = used + take;
                        int newMx = Math.max(mx, take);
                        ndp[newUsed][newMx] = Math.max(
                            ndp[newUsed][newMx],
                            dp[used][mx] + prefix[g][take]
                        );
                    }
                }
            }
            dp = ndp;
        }

        long ans = 0;
        for (int mx = 0; mx <= D; mx++) {
            if (dp[D][mx] <= Long.MIN_VALUE / 8) continue;
            int penaltyPairs = Math.max(0, 2 * mx - D - 1);
            long score = dp[D][mx] - 1L * penaltyPairs * P;
            ans = Math.max(ans, score);
        }

        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int D = sc.nextInt();
        int K = sc.nextInt();
        int P = sc.nextInt();

        int[][] films = new int[N][2];
        for (int i = 0; i < N; i++) {
            films[i][0] = sc.nextInt(); // genre
            films[i][1] = sc.nextInt(); // appeal
        }

        System.out.println(solve(N, D, K, P, films));
    }
}
```

---

# **Python Version (Cleaner for Students)**

```python id="y0xevf"
def solve(N, D, K, P, films):
    genre_films = [[] for _ in range(K + 1)]

    for g, a in films:
        genre_films[g].append(a)

    for g in range(1, K + 1):
        genre_films[g].sort(reverse=True)

    prefix = [[0] * (D + 1) for _ in range(K + 1)]
    for g in range(1, K + 1):
        for i in range(1, min(D, len(genre_films[g])) + 1):
            prefix[g][i] = prefix[g][i - 1] + genre_films[g][i - 1]

    NEG = -10**18
    dp = [[NEG] * (D + 1) for _ in range(D + 1)]
    dp[0][0] = 0

    for g in range(1, K + 1):
        ndp = [[NEG] * (D + 1) for _ in range(D + 1)]
        sz = min(D, len(genre_films[g]))

        for used in range(D + 1):
            for mx in range(D + 1):
                if dp[used][mx] == NEG:
                    continue

                for take in range(sz + 1):
                    if used + take > D:
                        break
                    new_used = used + take
                    new_mx = max(mx, take)
                    ndp[new_used][new_mx] = max(
                        ndp[new_used][new_mx],
                        dp[used][mx] + prefix[g][take]
                    )

        dp = ndp

    ans = 0
    for mx in range(D + 1):
        if dp[D][mx] == NEG:
            continue
        penalty_pairs = max(0, 2 * mx - D - 1)
        score = dp[D][mx] - penalty_pairs * P
        ans = max(ans, score)

    return ans


# Input
N = int(input())
D = int(input())
K = int(input())
P = int(input())

films = [tuple(map(int, input().split())) for _ in range(N)]

print(solve(N, D, K, P, films))
```

---

# **Concepts Covered**

This is a very good **hard-level hybrid problem** based on:

* **Dynamic Programming**
* **Grouping by category**
* **Prefix sums**
* **Greedy arrangement insight**
* **Scheduling optimization**
* **Counting unavoidable adjacency penalties**

---

# **Difficulty Level**

This is realistically:

* **LeetCode Hard**
* **Codeforces Div 2 D / Div 1 A-ish**
* **GeeksforGeeks Hard**
* **Good campus OA hard problem**

---

# **Best Practice Topics for Students**

To prepare for this problem, students should practice:

## **Must Know**

* Knapsack DP
* DP on groups
* Prefix sums
* Rearrangement / greedy spacing
* “No adjacent same” style logic

## **Related Search Keywords**

Search these on platforms:

```text id="2gpn7v"
group dp selection problem
knapsack with categories
rearrange to avoid adjacent equal
maximize score with penalty
top k from each group dp
```

---

# **Important Note for Your Sheet**

This is a **very good “Hard” custom problem**, but if you give it to students directly, I’d recommend also giving them this hint:

> **Hint:**
> First decide **how many films to take from each genre**, then think about how to **arrange genres** to minimize same-genre adjacency penalties.

That makes it challenging but still fair.

---


