# Set 4

---

### 15. **Check if a Binary Tree is a Binary Search Tree (BST)**

**Problem**:  
Given a binary tree, check whether it is a binary search tree (BST). In a BST, for every node, the value of all the nodes in the left subtree is less than the node's value, and the value of all the nodes in the right subtree is greater than the node's value.

**Input Format**:  
- The first line contains an integer `n` (number of nodes in the binary tree).
- The second line contains `n` space-separated integers representing the nodes of the binary tree in level order (use -1 to represent null nodes).

**Output Format**:  
- Print "YES" if the tree is a valid BST, otherwise print "NO".

**Sample Input**:
```
7
2 1 3 -1 -1 -1 -1
```

**Sample Output**:
```
YES
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class CheckBST {
    public static boolean isValidBST(TreeNode root, Integer min, Integer max) {
        if (root == null) return true;
        if ((min != null && root.val <= min) || (max != null && root.val >= max)) return false;
        return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
    }
    
    public static TreeNode buildTree(int[] arr, int n) {
        if (n == 0 || arr[0] == -1) return null;
        
        TreeNode root = new TreeNode(arr[0]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        int i = 1;
        while (!queue.isEmpty() && i < n) {
            TreeNode current = queue.poll();
            if (arr[i] != -1) {
                current.left = new TreeNode(arr[i]);
                queue.add(current.left);
            }
            i++;
            if (i < n && arr[i] != -1) {
                current.right = new TreeNode(arr[i]);
                queue.add(current.right);
            }
            i++;
        }
        return root;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] tree = new int[n];
        for (int i = 0; i < n; i++) {
            tree[i] = sc.nextInt();
        }
        
        TreeNode root = buildTree(tree, n);
        if (isValidBST(root, null, null)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
```

**Solution in Python**:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, min_val, max_val):
    if not root:
        return True
    if (min_val is not None and root.val <= min_val) or (max_val is not None and root.val >= max_val):
        return False
    return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)

def build_tree(arr):
    if not arr or arr[0] == -1:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if arr[i] != -1:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] != -1:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

n = int(input())
tree = list(map(int, input().split()))

root = build_tree(tree)
if is_valid_bst(root, None, None):
    print("YES")
else:
    print("NO")
```

---

### 16. **Find the Level Order Traversal of a Binary Tree**

**Problem**:  
Given a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

**Input Format**:  
- The first line contains an integer `n` (number of nodes in the binary tree).
- The second line contains `n` space-separated integers representing the nodes of the binary tree in level order (use -1 to represent null nodes).

**Output Format**:  
- Print the nodes in level order.

**Sample Input**:
```
7
3 9 20 -1 -1 15 7
```

**Sample Output**:
```
3 9 20 15 7
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class LevelOrderTraversal {
    public static List<Integer> levelOrder(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            result.add(node.val);
            if (node.left != null) queue.add(node.left);
            if (node.right != null) queue.add(node.right);
        }
        return result;
    }
    
    public static TreeNode buildTree(int[] arr, int n) {
        if (n == 0 || arr[0] == -1) return null;
        
        TreeNode root = new TreeNode(arr[0]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        int i = 1;
        while (!queue.isEmpty() && i < n) {
            TreeNode current = queue.poll();
            if (arr[i] != -1) {
                current.left = new TreeNode(arr[i]);
                queue.add(current.left);
            }
            i++;
            if (i < n && arr[i] != -1) {
                current.right = new TreeNode(arr[i]);
                queue.add(current.right);
            }
            i++;
        }
        return root;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] tree = new int[n];
        for (int i = 0; i < n; i++) {
            tree[i] = sc.nextInt();
        }
        
        TreeNode root = buildTree(tree, n);
        List<Integer> result = levelOrder(root);
        
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
```

**Solution in Python**:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def build_tree(arr):
    if not arr or arr[0] == -1:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if arr[i] != -1:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] != -1:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

n = int(input())
tree = list(map(int, input().split()))

root = build_tree(tree)
result = level_order(root)
print(" ".join(map(str, result)))
```

---

### 17. **Find the Kth Largest Element in an Array**

**Problem**:  
Given an array `arr` of `n` integers and an integer `k`, find the `k`-th largest element in the array.

**Input Format**:  
- The first line contains an integer `n` (size of the array).
- The second line contains `n` space-separated integers (the elements of the array).
- The third line contains an integer `k`.

**Output Format**:  
- Print the `k`-th largest element.

**Sample Input**:
```
6
3 2 1 5 6 4
2
```

**Sample Output**:
```
5
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.*;

public class KthLargest {
    public static int findKth

Largest(int[] arr, int k) {
        Arrays.sort(arr);
        return arr[arr.length - k];
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        
        System.out.println(findKthLargest(arr, k));
    }
}
```

**Solution in Python**:
```python
def find_kth_largest(arr, k):
    arr.sort()
    return arr[-k]

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(find_kth_largest(arr, k))
```

---

