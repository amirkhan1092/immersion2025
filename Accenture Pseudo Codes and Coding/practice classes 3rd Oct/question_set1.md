# Set-1

---

### 1. **Reverse a String**

**Problem**:  
Given a string of length `n`, write a program that reverses it.

**Input Format**:  
- The first line contains an integer `n` (length of the string).
- The second line contains a string `s` of length `n`.

**Output Format**:  
- A single string, which is the reverse of the input string.

**Sample Input**:
```
5
hello
```

**Sample Output**:
```
olleh
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.Scanner;

public class ReverseString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine(); // consume newline
        String s = sc.nextLine();
        System.out.println(new StringBuilder(s).reverse().toString());
    }
}
```

**Solution in Python**:
```python
n = int(input())
s = input()
print(s[::-1])
```

---

### 2. **Find the Maximum Element in an Array**

**Problem**:  
Given an array of `n` integers, find the maximum element.

**Input Format**:  
- The first line contains an integer `n` (size of the array).
- The second line contains `n` integers.

**Output Format**:  
- A single integer representing the maximum element in the array.

**Sample Input**:
```
5
1 5 3 9 2
```

**Sample Output**:
```
9
```

**Constraints**:  
- `1 <= n <= 1000`
- `-10^6 <= arr[i] <= 10^6`

**Solution in Java**:
```java
import java.util.Scanner;

public class MaxElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int max = Integer.MIN_VALUE;
        
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        System.out.println(max);
    }
}
```

**Solution in Python**:
```python
n = int(input())
arr = list(map(int, input().split()))
print(max(arr))
```

---

### 3. **Check if a String is a Palindrome**

**Problem**:  
Given a string of length `n`, check if it is a palindrome.

**Input Format**:  
- The first line contains an integer `n` (length of the string).
- The second line contains a string `s` of length `n`.

**Output Format**:  
- `True` if the string is a palindrome, `False` otherwise.

**Sample Input**:
```
5
madam
```

**Sample Output**:
```
True
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine(); // consume newline
        String s = sc.nextLine();
        
        if (s.equals(new StringBuilder(s).reverse().toString())) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}
```

**Solution in Python**:
```python
n = int(input())
s = input()
print(s == s[::-1])
```

---

### 4. **Find the Missing Number in an Array**

**Problem**:  
Given an array of `n` distinct numbers taken from `0, 1, 2, ..., n`, find the one number that is missing from the array.

**Input Format**:  
- The first line contains an integer `n` (size of the array).
- The second line contains `n` integers.

**Output Format**:  
- A single integer, which is the missing number.

**Sample Input**:
```
3
3 0 1
```

**Sample Output**:
```
2
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.Scanner;

public class MissingNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0, expectedSum = n * (n + 1) / 2;
        
        for (int i = 0; i < n; i++) {
            sum += sc.nextInt();
        }
        
        System.out.println(expectedSum - sum);
    }
}
```

**Solution in Python**:
```python
n = int(input())
arr = list(map(int, input().split()))
print(n * (n + 1) // 2 - sum(arr))
```

---

### 5. **Find the Intersection of Two Arrays**

**Problem**:  
Given two arrays, write a program to compute their intersection (common elements). The result should not contain any duplicates.

**Input Format**:  
- The first line contains an integer `n` (size of the first array).
- The second line contains `n` integers.
- The third line contains an integer `m` (size of the second array).
- The fourth line contains `m` integers.

**Output Format**:  
- A list of integers representing the intersection of the two arrays. The output should be in any order.

**Sample Input**:
```
4
1 2 2 1
2
2 2
```

**Sample Output**:
```
2
```

**Constraints**:  
- `1 <= n, m <= 1000`

**Solution in Java**:
```java
import java.util.*;

public class ArrayIntersection {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Set<Integer> set = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            set.add(sc.nextInt());
        }
        
        int m = sc.nextInt();
        Set<Integer> result = new HashSet<>();
        for (int i = 0; i < m; i++) {
            int num = sc.nextInt();
            if (set.contains(num)) {
                result.add(num);
            }
        }
        
        for (int num : result) {
            System.out.println(num);
        }
    }
}
```

**Solution in Python**:
```python
n = int(input())
arr1 = set(map(int, input().split()))
m = int(input())
arr2 = set(map(int, input().split()))
print(' '.join(map(str, arr1 & arr2)))
```

---