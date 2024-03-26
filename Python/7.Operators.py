"""Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators


Operator	Name	Example	Try it

"""

# Arithmetic operators
a = 5
b = 10
print("Arithmetic operators")

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # Remainder
print(a ** b) # a to the power b
print(a // b) # Quiescent

# Comparison Operators
x = 10
y = 50
z = 10
print("Comparison Operators")

print(x == z) # Equal
print(x != y) # Not equal
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) #Greater than or equal to
print(x <= y) # Less than or equal to

"""Logical operators
 AND and OR 
 AND = all condition need to be satisfied 
 OR = One condition need to be satisfied 
 NOT 
"""
# example AND
print("Logical operators",)

print(x==z and x<y)
print(not (x==z and x<y))
print(x==y and x<y)
print(x!=z or x==z)
print(not (x!=z or x==z))

"""Identity operators are used to compare the objects, 
not if they are equal, 
but if they are actually the same object, 
with the same memory location:
 """
print("Identity operators")

print(x is y) #Returns False if both variables are the same object
print(x is x) #Returns True if both variables are the same object
print(x is not y) #Returns True if both variables are not the same object

"""Membership operators are used to test if a sequence is presented in an object:
"""
print("Membership operators")

myList = ["a","b","c"]
print("a" in myList,)
print("x" in myList)
# returns True because a sequence with the value "a" is in the list and return False because "x" is not in the list.
print("a" not in myList) # False
print("x" not in myList) # Ture

# Bitwise operators are used to compare (binary) numbers:
print("Bitwise operators")

print(6 & 3)

"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010 <---set it to 1 if both are 1, otherwise it is set to 0
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111


& 	AND	
|	OR	
^	XOR	
~	NOT	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""
