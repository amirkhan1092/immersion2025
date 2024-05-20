# 
'''
This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, 
or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. 
Create an algorithm to find the nth sevenish number.
'''

n = int(input('Enter the nth value '))


# #  5 == 0101 (7^2 + 7^0) = 50
# element_value = 0
# for i, v in enumerate(bin(n)[2:][::-1]):
#     if v == '1':
#         element_value += 7 ** i 
# print(element_value)

element_value = 0
index = 0
while n:
    if n & 1:
        element_value += 7 ** index
    index += 1
    n >>= 1
print(element_value)    