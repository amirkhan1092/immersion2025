**pseudo code** questions focused on **ceil** and **floor** values:

---

### **Question 1:**
```pseudo
function calculateCeilFloor(x):
    if x mod 1 == 0 then
        return x, x
    else if x > 0 then
        ceil_val = x - (x mod 1) + 1
        floor_val = x - (x mod 1)
    else
        ceil_val = x - (x mod 1)
        floor_val = x - (x mod 1) - 1
    end if
    return ceil_val, floor_val
end function

x = -4.7
output = calculateCeilFloor(x)
```
**What are the values of `ceil_val` and `floor_val` for `x = -4.7`?**

---

### **Question 2:**
```pseudo
function nearestFloorCeil(A, n, X):
    left = 0
    right = n - 1
    while left <= right do:
        mid = (left + right) div 2
        if A[mid] = X then
            return A[mid], A[mid]
        else if A[mid] < X then
            left = mid + 1
        else
            right = mid - 1
        end if
    end while
    return A[right], A[left]
end function

A = [1, 4, 6, 9, 12]
X = 8
output = nearestFloorCeil(A, 5, X)
```
**Find the floor and ceil of `X = 8` in the array.**

---

### **Question 3:**
```pseudo
function ceilFloorSum(N):
    sum_ceil = 0
    sum_floor = 0
    for i = 1 to N do:
        sum_ceil = sum_ceil + ceil(N/i)
        sum_floor = sum_floor + floor(N/i)
    end for
    return sum_ceil, sum_floor
end function

N = 10
output = ceilFloorSum(N)
```
**What are the values of `sum_ceil` and `sum_floor` for `N = 10`?**

---

### **Question 4:**
```pseudo
function modifiedCeilFloor(x):
    if x = 0 then
        return 0, 0
    else if x > 0 then
        return floor(x * 2) / 2, ceil(x * 2) / 2
    else
        return ceil(x * 2) / 2, floor(x * 2) / 2
    end if
end function

x = 5.3
output = modifiedCeilFloor(x)
```
**What is the result of `modifiedCeilFloor(5.3)`?**

---

### **Question 5:**
```pseudo
function ceilFloorPow(x, y):
    result = x ^ y
    return ceil(result), floor(result)
end function

x = 2.5
y = 3
output = ceilFloorPow(x, y)
```
**What are the `ceil` and `floor` values for `x = 2.5` raised to the power `y = 3`?**

---

### **Question 6:**
```pseudo
function ceilFloorModulo(A, B):
    if B = 0 then
        return None
    else
        result = A / B
        return ceil(result), floor(result)
    end if
end function

A = 17
B = 4
output = ceilFloorModulo(A, B)
```
**What is the result of `ceilFloorModulo(17, 4)`?**

---

### **Question 7:**
```pseudo
function alternatingCeilFloor(N):
    sum_ceil = 0
    sum_floor = 0
    for i = 1 to N do:
        if i mod 2 = 0 then
            sum_ceil = sum_ceil + ceil(i / 2)
        else
            sum_floor = sum_floor + floor(i / 2)
        end if
    end for
    return sum_ceil, sum_floor
end function

N = 9
output = alternatingCeilFloor(N)
```
**What are the values of `sum_ceil` and `sum_floor` when `N = 9`?**

---

### **Question 8:**
```pseudo
function ceilFloorNested(x, y):
    result = x / y
    return ceil(floor(result) + ceil(result)), floor(ceil(result) + floor(result))
end function

x = 6.7
y = 2.3
output = ceilFloorNested(x, y)
```
**What is the output of `ceilFloorNested(6.7, 2.3)`?**

---

### **Question 9:**
```pseudo
function iterativeCeilFloor(n, x):
    result = 1
    for i = 1 to n do:
        if i mod 2 = 0 then
            result = result * ceil(x / i)
        else
            result = result * floor(x / i)
        end if
    end for
    return result
end function

n = 5
x = 7.8
output = iterativeCeilFloor(n, x)
```
**What is the final value of `result` after executing `iterativeCeilFloor(5, 7.8)`?**

---

### **Question 10:**
```pseudo
function ceilFloorInArray(A, n):
    total_ceil = 0
    total_floor = 0
    for i = 0 to n-1 do:
        total_ceil = total_ceil + ceil(A[i])
        total_floor = total_floor + floor(A[i])
    end for
    return total_ceil, total_floor
end function

A = [1.2, 3.8, -2.5, 4.6]
output = ceilFloorInArray(A, 4)
```
**What is the result of `ceilFloorInArray([1.2, 3.8, -2.5, 4.6], 4)`?**

---

These questions challenge students on different ways of using **ceil** and **floor** values in complex logical scenarios.