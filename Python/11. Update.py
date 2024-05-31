#UPDATE


#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.
# You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.

#ADD to TUPLE

thisTuple = ("apple","banana","orange")
#change tuple to list
x = list(thisTuple)
#add value
x.append("carrot")
#change list back to tuple
thisTuple = tuple(x)
print((thisTuple))

#Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item,
# (or many), create a new tuple with the item(s), and add it to the existing tuple:

thisTuple = (1,2,3,4,5)
thatTuple = (6,7,8,9,10)

addTuple = thisTuple+thatTuple
print(addTuple)

"""Note: When creating a tuple with only one item, 
remember to include a comma after the item, otherwise it will not be identified as a tuple. 
tuple("apple", ) 
"""

#REMOVE ITEMS FROM TUPLE
"""Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:"""

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#DELETE TUPLE
#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) --- this will raise an error because the tuple no longer exists


print("--------------------------SETS------------------------")
"""
Update
The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.
"""

#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Note: Both union() and update() will exclude any duplicate items.


