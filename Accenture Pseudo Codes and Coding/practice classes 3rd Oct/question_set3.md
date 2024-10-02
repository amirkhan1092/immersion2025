# Set 3

---

### 12. **Implement a Stack Using an Array**

**Problem**:  
Implement a stack using an array, supporting the following operations: push, pop, and peek.

**Input Format**:  
- The first line contains an integer `n` (number of operations).
- The next `n` lines contain one of three commands: 
  - "push x" (where `x` is an integer to be pushed onto the stack)
  - "pop" (which removes the top element from the stack)
  - "peek" (which returns the top element of the stack without removing it)

**Output Format**:  
- For each "peek" command, output the top element of the stack. 
- If the stack is empty when a "pop" or "peek" is called, print "Empty Stack".

**Sample Input**:
```
5
push 3
push 5
peek
pop
peek
```

**Sample Output**:
```
5
3
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.*;

public class StackUsingArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        int n = sc.nextInt();
        sc.nextLine();  // consume the newline
        
        for (int i = 0; i < n; i++) {
            String command = sc.nextLine();
            if (command.startsWith("push")) {
                int x = Integer.parseInt(command.split(" ")[1]);
                stack.push(x);
            } else if (command.equals("pop")) {
                if (stack.isEmpty()) {
                    System.out.println("Empty Stack");
                } else {
                    stack.pop();
                }
            } else if (command.equals("peek")) {
                if (stack.isEmpty()) {
                    System.out.println("Empty Stack");
                } else {
                    System.out.println(stack.peek());
                }
            }
        }
    }
}
```

**Solution in Python**:
```python
n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if stack:
            stack.pop()
        else:
            print("Empty Stack")
    elif command[0] == "peek":
        if stack:
            print(stack[-1])
        else:
            print("Empty Stack")
```

---

### 13. **Implement a Queue Using an Array**

**Problem**:  
Implement a queue using an array, supporting the following operations: enqueue, dequeue, and front.

**Input Format**:  
- The first line contains an integer `n` (number of operations).
- The next `n` lines contain one of three commands: 
  - "enqueue x" (where `x` is an integer to be added to the queue)
  - "dequeue" (which removes the front element from the queue)
  - "front" (which returns the front element without removing it)

**Output Format**:  
- For each "front" command, output the front element of the queue.
- If the queue is empty when "dequeue" or "front" is called, print "Empty Queue".

**Sample Input**:
```
5
enqueue 3
enqueue 5
front
dequeue
front
```

**Sample Output**:
```
3
5
```

**Constraints**:  
- `1 <= n <= 1000`

**Solution in Java**:
```java
import java.util.*;

public class QueueUsingArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> queue = new LinkedList<>();
        int n = sc.nextInt();
        sc.nextLine();  // consume the newline
        
        for (int i = 0; i < n; i++) {
            String command = sc.nextLine();
            if (command.startsWith("enqueue")) {
                int x = Integer.parseInt(command.split(" ")[1]);
                queue.add(x);
            } else if (command.equals("dequeue")) {
                if (queue.isEmpty()) {
                    System.out.println("Empty Queue");
                } else {
                    queue.poll();
                }
            } else if (command.equals("front")) {
                if (queue.isEmpty()) {
                    System.out.println("Empty Queue");
                } else {
                    System.out.println(queue.peek());
                }
            }
        }
    }
}
```

**Solution in Python**:
```python
n = int(input())
queue = []

for _ in range(n):
    command = input().split()
    
    if command[0] == "enqueue":
        queue.append(int(command[1]))
    elif command[0] == "dequeue":
        if queue:
            queue.pop(0)
        else:
            print("Empty Queue")
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print("Empty Queue")
```

---

### 14. **Find the Lowest Common Ancestor in a Binary Tree**

**Problem**:  
Given a binary tree and two nodes, find the lowest common ancestor (LCA) of these two nodes. The LCA of two nodes `p` and `q` is the lowest node that has both `p` and `q` as descendants.

**Input Format**:  
- The first line contains an integer `n` (number of nodes in the binary tree).
- The second line contains `n` space-separated integers representing the nodes of the binary tree in level order (use -1 to represent null nodes).
- The third line contains two integers `p` and `q` (the two nodes whose LCA is to be found).

**Output Format**:  
- A single integer representing the LCA of `p` and `q`.

**Sample Input**:
```
7
3 5 1 6 2 0 8
5 1
```

**Sample Output**:
```
3
```

**Constraints**:  
- `1 <= n <= 1000`
- All node values are unique.

**Solution in Java**:
```java
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class LCA {
    public static TreeNode lca(TreeNode root, int p, int q) {
        if (root == null || root.val == p || root.val == q) {
            return root;
        }
        TreeNode left = lca(root.left, p, q);
        TreeNode right = lca(root.right, p, q);
        if (left != null && right != null) {
            return root;
        }
        return left != null ? left : right;
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
        int p = sc.nextInt();
        int q = sc.nextInt();
        
        TreeNode root = buildTree(tree, n);
        TreeNode ancestor = lca(root, p, q);
        
        if (ancestor != null) {
            System.out.println(ancestor.val);
        } else {
            System.out.println("No LCA found");
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

def lca(root, p, q):
    if not root or root.val == p or root.val == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right

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
tree = list(map

(int, input().split()))
p, q = map(int, input().split())

root = build_tree(tree)
ancestor = lca(root, p, q)

if ancestor:
    print(ancestor.val)
else:
    print("No LCA found")
```

---

Let me know if you'd like me to continue!