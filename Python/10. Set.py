"""
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.

 Note: Set items are unchangeable, but you can remove items and add new items.
 Sets are written with curly brackets.{}
"""

#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)
#Note: Sets are unordered, so you cannot be sure in which order the items will appear.

"""
1. Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

2. Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.


3. Duplicates Not Allowed
Sets cannot have two items with the same value.

"""
thisset = {3,3,4,4,9,9}
print(thisset)
#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {1,1,True,"2","apple"}
print(thisset)
#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {0,0,False,"2","apple"}
print(thisset)

#length of the set

print(len(thisset))

# find of data type of set
print(type(thisset))

# Make set constructor
thisset = set((1,4,3,2,4,5))  # note the double round-brackets()  not the curly brackets{}
print(thisset)
