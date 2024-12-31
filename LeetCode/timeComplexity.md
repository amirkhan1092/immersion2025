Here are 10 coding questions designed to help you understand time complexity, complete with example solutions and explanations:

---

### **1. Find the Maximum Element in an Array**
**Problem:** Write a function to find the maximum element in an array.  
**Time Complexity:** \( O(n) \)

```python
def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Example
arr = [1, 3, 5, 2, 4]
print(find_max(arr))  # Output: 5
```

**Explanation:** The function iterates through the array once, so the time complexity is linear.

---

### **2. Check if an Array is Sorted**
**Problem:** Write a function to check if an array is sorted in ascending order.  
**Time Complexity:** \( O(n) \)

```python
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  # Output: True
```

**Explanation:** The function performs a single pass through the array, making comparisons between adjacent elements.

---

### **3. Count Pairs with a Given Sum**
**Problem:** Find the number of pairs in an array that sum up to a given value.  
**Time Complexity:** \( O(n^2) \)

```python
def count_pairs(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1
    return count

# Example
arr = [1, 2, 3, 4]
target = 5
print(count_pairs(arr, target))  # Output: 2
```

**Explanation:** The nested loops result in a quadratic time complexity.

---

### **4. Binary Search**
**Problem:** Implement binary search on a sorted array to find a target value.  
**Time Complexity:** \( O(\log n) \)

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
arr = [1, 2, 3, 4, 5]
target = 4
print(binary_search(arr, target))  # Output: 3
```

**Explanation:** The array is halved in each iteration, leading to logarithmic time complexity.

---

### **5. Reverse a String**
**Problem:** Reverse a string.  
**Time Complexity:** \( O(n) \)

```python
def reverse_string(s):
    return s[::-1]

# Example
s = "hello"
print(reverse_string(s))  # Output: "olleh"
```

**Explanation:** Slicing iterates through the string once.

---

### **6. Find Duplicate in an Array**
**Problem:** Find if there is any duplicate in an array.  
**Time Complexity:** \( O(n^2) \) or \( O(n) \) with hashing.

```python
def has_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example
arr = [1, 2, 3, 4, 2]
print(has_duplicate(arr))  # Output: True
```

**Explanation:** Using a hash set allows \( O(1) \) average-time insert and lookup, making the overall complexity linear.

---

### **7. Merge Two Sorted Arrays**
**Problem:** Merge two sorted arrays into a single sorted array.  
**Time Complexity:** \( O(n + m) \)

```python
def merge_sorted(arr1, arr2):
    i, j = 0, 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

# Example
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]
```

**Explanation:** The function iterates through both arrays once.

---

### **8. Find the First Non-Repeating Character**
**Problem:** Find the first character in a string that does not repeat.  
**Time Complexity:** \( O(n) \) with \( O(1) \) space for fixed alphabet size.

```python
from collections import Counter

def first_non_repeating(s):
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Example
s = "swiss"
print(first_non_repeating(s))  # Output: "w"
```

**Explanation:** Counting characters takes \( O(n) \), and traversing again to find the first unique character also takes \( O(n) \).

---

### **9. Find All Prime Numbers Less than N**
**Problem:** Use the Sieve of Eratosthenes to find all prime numbers less than \( n \).  
**Time Complexity:** \( O(n \log(\log n)) \)

```python
def sieve_of_eratosthenes(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

# Example
n = 20
print(sieve_of_eratosthenes(n))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
```

**Explanation:** The algorithm efficiently eliminates multiples of primes.

---

### **10. Generate Fibonacci Numbers**
**Problem:** Generate the first \( n \) Fibonacci numbers.  
**Time Complexity:** \( O(n) \)

```python
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Example
n = 10
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Explanation:** The function iteratively computes the Fibonacci sequence, resulting in linear complexity.

---

These questions provide a mix of scenarios to understand and analyze different time complexities.
