# Set 2
---

### 6. **Remove Duplicates from an Array**

**Problem**:  
Given an array of integers, write a program to remove the duplicates and return the unique elements.

**Input Format**:  
- The first line contains an integer `n` (size of the array).
- The second line contains `n` integers.

**Output Format**:  
- A list of integers without duplicates, in any order.

**Sample Input**:
```
5
1 2 2 3 4
```

**Sample Output**:
```
1 2 3 4
```

**Constraints**:  
- `1 <= n <= 1000`
- `-10^6 <= arr[i] <= 10^6`

**Solution in Java**:
```java
import java.util.*;

public class RemoveDuplicates {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Set<Integer> set = new LinkedHashSet<>();
        
        for (int i = 0; i < n; i++) {
            set.add(sc.nextInt());
        }
        
        for (int num : set) {
            System.out.print(num + " ");
        }
    }
}
```

**Solution in Python**:
```python
n = int(input())
arr = list(map(int, input().split()))
print(' '.join(map(str, sorted(set(arr)))))
```

---

### 7. **Count the Occurrence of Each Element in an Array**

**Problem**:  
Given an array of integers, count how many times each unique element appears in the array.

**Input Format**:  
- The first line contains an integer `n` (size of the array).
- The second line contains `n` integers.

**Output Format**:  
- A list of integers with their counts, in the order they first appear.

**Sample Input**:
```
5
1 2 2 3 3
```

**Sample Output**:
```
1 1
2 2
3 2
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.*;

public class CountOccurrences {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<Integer, Integer> countMap = new LinkedHashMap<>();
        
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
```

**Solution in Python**:
```python
n = int(input())
arr = list(map(int, input().split()))
count = {}
for num in arr:
    count[num] = count.get(num, 0) + 1
for key, value in count.items():
    print(key, value)
```

---

### 8. **Find the Second Largest Element in an Array**

**Problem**:  
Given an array of integers, find the second largest element.

**Input Format**:  
- The first line contains an integer `n` (size of the array).
- The second line contains `n` integers.

**Output Format**:  
- A single integer, which is the second largest element.

**Sample Input**:
```
5
1 3 4 2 5
```

**Sample Output**:
```
4
```

**Constraints**:  
- `2 <= n <= 1000`

**Solution in Java**:
```java
import java.util.*;

public class SecondLargest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        Arrays.sort(arr);
        System.out.println(arr[n-2]);
    }
}
```

**Solution in Python**:
```python
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(set(arr))
print(arr[-2])
```

---

### 9. **Merge Two Sorted Arrays**

**Problem**:  
Given two sorted arrays, merge them into one sorted array.

**Input Format**:  
- The first line contains an integer `n` (size of the first array).
- The second line contains `n` integers in sorted order.
- The third line contains an integer `m` (size of the second array).
- The fourth line contains `m` integers in sorted order.

**Output Format**:  
- A single line containing all integers from both arrays, in sorted order.

**Sample Input**:
```
3
1 3 5
3
2 4 6
```

**Sample Output**:
```
1 2 3 4 5 6
```

**Constraints**:  
- `1 <= n, m <= 1000`

**Solution in Java**:
```java
import java.util.*;

public class MergeSortedArrays {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr1 = new int[n];
        for (int i = 0; i < n; i++) {
            arr1[i] = sc.nextInt();
        }
        
        int m = sc.nextInt();
        int[] arr2 = new int[m];
        for (int i = 0; i < m; i++) {
            arr2[i] = sc.nextInt();
        }
        
        int[] merged = new int[n + m];
        System.arraycopy(arr1, 0, merged, 0, n);
        System.arraycopy(arr2, 0, merged, n, m);
        
        Arrays.sort(merged);
        for (int num : merged) {
            System.out.print(num + " ");
        }
    }
}
```

**Solution in Python**:
```python
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
print(' '.join(map(str, sorted(arr1 + arr2))))
```

---

### 10. **Find the Length of the Longest Substring Without Repeating Characters**

**Problem**:  
Given a string, find the length of the longest substring without repeating characters.

**Input Format**:  
- The first line contains an integer `n` (length of the string).
- The second line contains a string `s` of length `n`.

**Output Format**:  
- A single integer, which is the length of the longest substring without repeating characters.

**Sample Input**:
```
8
abcabcbb
```

**Sample Output**:
```
3
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.*;

public class LongestSubstring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();  // consume newline
        String s = sc.nextLine();
        
        Set<Character> set = new HashSet<>();
        int maxLength = 0, left = 0;
        
        for (int right = 0; right < n; right++) {
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        System.out.println(maxLength);
    }
}
```

**Solution in Python**:
```python
n = int(input())
s = input()
char_set = set()
max_length = 0
left = 0

for right in range(n):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)
```

---

### 11. **Reverse a Linked List**

**Problem**:  
Given a singly linked list, reverse the list and return the head of the reversed list.

**Input Format**:  
- The first line contains an integer `n` (size of the linked list).
- The second line contains `n` integers representing the linked list.

**Output Format**:  
- A list of integers representing the reversed linked list.

**Sample Input**:
```
5
1 2 3 4 5
```

**Sample Output**:
```
5 4 3 2 1
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class ReverseLinkedList {
    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
   

 }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        for (int i = 0; i < n; i++) {
            current.next = new ListNode(sc.nextInt());
            current = current.next;
        }
        
        ListNode reversedHead = reverseList(dummy.next);
        
        while (reversedHead != null) {
            System.out.print(reversedHead.val + " ");
            reversedHead = reversedHead.next;
        }
    }
}
```

**Solution in Python**:
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

n = int(input())
vals = list(map(int, input().split()))

dummy = ListNode(0)
current = dummy
for val in vals:
    current.next = ListNode(val)
    current = current.next

reversed_head = reverse_list(dummy.next)

while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next
```

---

