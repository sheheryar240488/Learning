"""
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

List items are indexed, the first item has index [0], the second item has index [1] etc.
"""
# example
mylist = ["apple", "banana", "cherry"]
print(mylist)

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#list length
print(len(list1))

#list type: From Python's perspective, lists are defined as "objects" with the data type 'list':
print(type(list1))

"""
What Does Constructor Mean?
A constructor is a special method of a class or structure in object-oriented programming that initializes a newly created object of that type. 
Whenever an object is created, the constructor is called automatically.

"""

# It is also possible to use the list() constructor when creating a new list.
thislist =list(("apple","orange","banana"))
print(thislist)

"""Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)

#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
