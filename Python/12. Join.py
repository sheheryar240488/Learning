#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Another way to join to list is Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

"""In this loop, we say: "For each number x in list2, do something."
And what's that something? Well, we're adding each number x from list2 to list1.
So, it goes like this:

Take the first number from list2, which is 1, and add it to list1.
Then, take the second number from list2, which is 2, and add it to list1.
Finally, take the third number from list2, which is 3, and add it to list1.
After that's all done, we print out list1 to see what it looks like now.

So, when we print list1, it will have the original letters "a", "b", and "c", plus the numbers 1, 2, and 3 added to the end. It will look like this:
"""
#Or you can use the extend() method, where the purpose is to add elements from one list to another list:
mylist = ["1","3","5"]
youlist = ["2","4","6"]
mylist.extend(youlist)
print("extend")
print(mylist)


print("#-------------------Tuples--------------------#")


thistuple = (1,2,3,4,5)
thattuple = (6,6,7,7,8)

x = thistuple+thattuple
print(x)

#Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

x = thistuple*5
print(x)


print("-----------------------SETS------------------------")

thisset = {1,"ali",2,3}
thatset = {6,7,99}

print(thisset.union(thatset))

"""Join Multiple Sets
All the joining methods and operators can be used to join multiple sets.

When using a method, just add more sets in the parentheses, separated by commas:

"""

#Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas"}

myset = set1.union(set2, set3, set4)
print(myset)

# When using the | operator, separate the sets with more | operators:
#Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

"""Join a SET and a Tuple

The union() method allows you to join a set with other data types, like lists or tuples.
The result will be a set.
"""

thistuple = [1,2,3]
thisset = {66,77,88}

print(thisset.union(thistuple))
#Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

#Note: Both union() and update() will exclude any duplicate items.


