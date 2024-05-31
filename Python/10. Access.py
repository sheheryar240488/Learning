#ACCESS



print("ACCESS TUPLE")
# You can access tuple items by referring to the index number, inside square brackets:
thisTuple = ("apple","banana","carrot")
print(thisTuple[1])

# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).Remember that the first item has index 0.

#Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



#----------------------SETS-----------------------#
print("----------------------SETS-----------------------")

thisset = {1,2,3,4,5,"apple"}
for x in thisset:
   print(x)

#find a value in set
print(3 in thisset)

#add to set
thisset.add("ali") #To add one item to a set use the add() method.


print(thisset)

#update the set
thisset.update([8,42])
print(thisset)

thisset.update(["Eight","Nine"])
print(thisset)

#To add items from another set into the current set, use the update() method.
#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#To remove an item in a set, use the remove(), or the discard() method.

thisset ={1,2,3,4,5,6}
thisset.remove(2)
print(thisset)
#Note: If the item to remove does not exist, remove() will raise an error.

#Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error.



#Remove a random item by using the pop() method:
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
print(x)
print(thisset)

#CLEAR the set

print(thisset.clear()) # answer None

#delete set
#The del keyword will delete the set completely:


del thisset
print(thisset)


