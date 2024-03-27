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