✅ Problem Restatement

**Given:** A sorted (increasing) array, rotated at some unknown pivot. No duplicates.
**Task:** Find the **minimum element** in O(log N) time.
**Example:**
Input: `[5, 7, 10, 3, 4]`
Output: `3`

---

### 🔍 Approach (Binary Search)

1. Let `low = 0`, `high = n - 1`.
2. While `low < high`:

   * Find `mid = (low + high) / 2`.
   * Compare `arr[mid]` with `arr[high]`.

     * If `arr[mid] > arr[high]`, the minimum is in the **right half** (excluding `mid`).
     * Else, the minimum is in the **left half** (including `mid`).
3. When `low == high`, that's the minimum.

---

### ✅ Java Code

```java
public class RotatedArrayMin {
    public static int findMin(int[] arr) {
        int low = 0;
        int high = arr.length - 1;

        while (low < high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] > arr[high]) {
                low = mid + 1; // Min must be to the right
            } else {
                high = mid; // Min could be at mid or to the left
            }
        }

        return arr[low]; // or arr[high], since low == high
    }

    public static void main(String[] args) {
        int[] arr = {5, 7, 10, 3, 4};
        System.out.println("Minimum element is: " + findMin(arr)); // Output: 3
    }
}
```

---

### 🧠 Time & Space Complexity

* **Time Complexity:** `O(log N)`
* **Space Complexity:** `O(1)`

---

### 🔁 Dry Run on `[5, 7, 10, 3, 4]`

* `low = 0`, `high = 4`, `mid = 2 → 10 > 4`, so `low = 3`
* `low = 3`, `high = 4`, `mid = 3 → 3 < 4`, so `high = 3`
* Now `low == high == 3`, return `arr[3] = 3`

