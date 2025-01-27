 

**Problem Title:** Merge K Sorted Arrays  

---

#### **Problem Statement**  
You are given `k` sorted arrays of integers. Your task is to merge these arrays into a single sorted array.  

Use a **Priority Queue (Min-Heap)** to efficiently manage the merging process.  

---

#### **Input Format**  
- An integer `k` (1 ≤ k ≤ 100): The number of sorted arrays.  
- An array of arrays, where each sub-array represents a sorted list of integers:  
  - The total number of elements across all arrays will not exceed 10^5.  

---

#### **Output Format**  
- Print the merged sorted array.  

---

#### **Example**  

**Input:**  
```  
3  
[1, 4, 7]  
[2, 5, 8]  
[3, 6, 9]  
```  

**Output:**  
```  
[1, 2, 3, 4, 5, 6, 7, 8, 9]  
```  

**Explanation:**  
The three sorted arrays are merged into a single sorted array:  
\[1, 2, 3, 4, 5, 6, 7, 8, 9\].  

---

#### **Approach**  

1. **Use a Min-Heap (Priority Queue):**  
   - Push the first element of each array into the heap along with the array index and the element index.  
   - Pop the smallest element from the heap and add it to the result.  
   - Push the next element of the same array into the heap.  

2. **Repeat Until the Heap is Empty:**  
   - Continue popping elements from the heap and pushing the next elements from the arrays into the heap.  

3. **Output the Result:**  
   - The result will contain all the elements in sorted order.  

---

#### **Solution Code**  

```java
import java.util.*;

public class MergeKSortedArrays {
    static class Element {
        int value;
        int arrayIndex;
        int elementIndex;

        public Element(int value, int arrayIndex, int elementIndex) {
            this.value = value;
            this.arrayIndex = arrayIndex;
            this.elementIndex = elementIndex;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input: number of arrays
        int k = sc.nextInt();
        List<List<Integer>> arrays = new ArrayList<>();

        // Input: each sorted array
        for (int i = 0; i < k; i++) {
            int n = sc.nextInt(); // size of the array
            List<Integer> arr = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                arr.add(sc.nextInt());
            }
            arrays.add(arr);
        }

        // Priority Queue (Min-Heap) based on the element value
        PriorityQueue<Element> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e.value));

        // Add the first element of each array to the heap
        for (int i = 0; i < arrays.size(); i++) {
            if (!arrays.get(i).isEmpty()) {
                pq.add(new Element(arrays.get(i).get(0), i, 0));
            }
        }

        List<Integer> result = new ArrayList<>();

        // Merge process
        while (!pq.isEmpty()) {
            Element current = pq.poll();
            result.add(current.value);

            // Get the next element from the same array, if available
            int nextIndex = current.elementIndex + 1;
            if (nextIndex < arrays.get(current.arrayIndex).size()) {
                pq.add(new Element(arrays.get(current.arrayIndex).get(nextIndex), current.arrayIndex, nextIndex));
            }
        }

        // Output the merged sorted array
        System.out.println(result);
    }
}
```  

---

#### **How It Works**  
1. **Initialize the Heap:** Push the first element of each array into the heap.  
2. **Merge Step:** Repeatedly extract the smallest element, adding it to the result, and push the next element from the same array.  
3. **Efficiency:** The heap ensures we always process the smallest element in \(O(\log k)\), where \(k\) is the number of arrays.  

---

#### **Sample Input/Output**  

**Input:**  
```  
4  
[1, 5, 10]  
[2, 6]  
[3, 4, 8]  
[7, 9]  
```  

**Output:**  
```  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
```  

#### **Edge Cases to Test**  
1. Arrays of unequal lengths.  
2. Arrays with duplicate elements.  
3. An input with one empty array.  

Let me know if you need further variations or help!
