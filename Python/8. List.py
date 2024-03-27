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


#Access the value in the list
print("#Access the value in the list ")

accessList = ["a","b","c","d","e","f"]
print(accessList[1])

#Slicing - Getting the required value for the list
print("#Slicing - Getting the required value for the list ")
print(accessList[2:5])
print(accessList[:5])
print(accessList[2:])

#Update the value in list
print("#Update the value in list")
accessList[2]="Hello"
print(accessList)

#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#The insert() method inserts an item at the specified index:
print("insert value")

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "BOOM")
print(thislist)

#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#ADD two lists.
print("ADD two lists")

one = [1,3,4]
two = [2,5,6]
addList = one + two
print(addList)


# CHANGE
print("#Change the value in the list ")
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#How to find the value in the list
print("Find the value in the list")

thislist = ["apple", "banana", "cherry"]
print("apple" in thislist)
#REMOVE VALUE

# The remove() method removes the specified item.
print("REMOVE specified item")

thislist = ["apple","banana","orange"]
thislist.remove(thislist[1])
print(thislist)

# you can also just add str you want to remove from the list
print("Remove from the list")

thislist = ["apple","banana","orange"]
thislist.remove("apple")
print(thislist)

#Remove a spicific index with pop().

thislist =["Ali","Bilal","Omar"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
thislist =["Ali","Bilal","Omar"]
thislist.pop()
print(thislist)

#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#del can delete list completly
thislist =["1",["shah","abc"]]
del thislist #dont print you will get an error. because the list is deleted.

#clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


things = ["apple","ball","cat","dog","fish"]
newlist = [x for x in things if "c" in x]
print(newlist)



