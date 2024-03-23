"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.
"""

# example

x = "Python"
y = 'learning'
print(x,y)

# You can assign a multiline string to a variable by using three quotes:

z = """ Hi my name is Sheheryar Shah. 
I am learning Python for test automation. 
"""
print(z)

# String Array
# Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = "Hello"
print(a[2])
# answer is l

# length of a string
print(len(a))
#5

# check if a word is in the string
print ("test" in z)
# true

# check if a phrase is not in the string
print("QA enginner" not in z)

# use if statement

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

if "world" not in txt:
    print("this word is not in the string")

if "best" not in txt:
    print("this word is not in the string")
else:
    print("statement is false and this word is present in the string")


# Slicing String

txt = "0123456789"
#      01234567)
print(txt[1:5])
print(txt[0:5])
print(txt[2:])
print(txt[:2])
print(txt[-5:-2])

# Modify String

# Upper case

txt = "Hello World"
print(txt.upper())

#Lower case
print(txt.lower())

#Remove white spaces
print(txt.strip())

#Split
print(txt.split("e"))
print(txt.split("o"))

#Replace
print(txt.replace("World","Denmark"))



