# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

"""
output by Python Shell as Chrome extension 
>>> a, b = 0, 1 
>>> while a < 17:
    print(a)
    a, b = b, a+b
... 
0
1
1
2
3
5
8
13
>>> print(b)
34
>>> print(a)
21
""" 
