**pseudo code** questions on **ceil** and **floor** values:

---

### **Question 1:**
```pseudo
x = 9.3
if x mod 1 = 0 then
    ceil_val = x
    floor_val = x
else
    ceil_val = x - (x mod 1) + 1
    floor_val = x - (x mod 1)
end if
// What are the values of ceil_val and floor_val for x = 9.3?
```

---

### **Question 2:**
```pseudo
A = [2.5, 7.1, 3.6, 4.9]
sum_ceil = 0
sum_floor = 0
for i = 0 to length(A) - 1 do:
    sum_ceil = sum_ceil + ceil(A[i])
    sum_floor = sum_floor + floor(A[i])
end for
// What are the values of sum_ceil and sum_floor for the array A?
```

---

### **Question 3:**
```pseudo
x = -5.6
if x mod 1 = 0 then
    ceil_val = x
    floor_val = x
else if x > 0 then
    ceil_val = x - (x mod 1) + 1
    floor_val = x - (x mod 1)
else
    ceil_val = x - (x mod 1)
    floor_val = x - (x mod 1) - 1
end if
// Find ceil_val and floor_val for x = -5.6.
```

---

### **Question 4:**
```pseudo
x = 8.4
ceil_val = x - (x mod 1) + 1
floor_val = x - (x mod 1)
// Calculate ceil_val and floor_val for x = 8.4.
```

---

### **Question 5:**
```pseudo
A = [1.2, 5.6, -3.4, 7.9]
total_ceil = 0
total_floor = 0
for i = 0 to length(A) - 1 do:
    total_ceil = total_ceil + ceil(A[i])
    total_floor = total_floor + floor(A[i])
end for
// What is the total_ceil and total_floor for the array A?
```

---

### **Question 6:**
```pseudo
x = 13.7
ceil_val = ceil(x / 2)
floor_val = floor(x / 2)
// What are the values of ceil_val and floor_val for x = 13.7?
```

---

### **Question 7:**
```pseudo
n = 4.8
result = 0
for i = 1 to 5 do:
    result = result + ceil(n / i) + floor(n / i)
end for
// Find the final result after the loop executes.
```

---

### **Question 8:**
```pseudo
x = 14.3
y = 3.5
temp_ceil = ceil(x / y)
temp_floor = floor(x / y)
// What are the values of temp_ceil and temp_floor for x = 14.3 and y = 3.5?
```

---

### **Question 9:**
```pseudo
x = 6.5
y = 3.2
result = ceil(x * y) + floor(x * y)
// Calculate the result for x = 6.5 and y = 3.2.
```

---

### **Question 10:**
```pseudo
x = -7.9
y = 2.4
ceil_val = ceil(x / y)
floor_val = floor(x / y)
// What are the values of ceil_val and floor_val for x = -7.9 and y = 2.4?
```

---

These pseudo code questions are structured to focus on **ceil** and **floor** calculations without involving functions, challenging students to interpret and manually compute the correct values in each scenario.