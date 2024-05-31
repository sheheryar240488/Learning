#You can loop through the list items by using a for loop:

#Iterate the  list value : Print all items in the list, one by one:
print("Iterate: Print one by one")

thislist = ["first","second","thrid"]
for x in thislist:
    print(x)

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple","banana","orange","mango"]
for x in fruits:
    print(x)
    if x == "orange":
        break

# While loop with list
print("WHILE loop")

x = ["Ibrahim","Shahid","Ali","Asad"]
y = 0
print(x)

while y < (len(x)):
    print(x[y])
    y = y + 1

print("LOOP WITH ----------------------------Tuples____________________________________")

"""You can loop through the tuple items by using a for loop."""

#one way of doing it is:

print("#one way of doing it is:")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Through index number
print("Print through index number")
thistuple = ("apple", "banana", "cherry")
y = 0
for x in thistuple:
    if y < len(thistuple):
        print(thistuple[y])
        y += 1

print("Through Range")
for i in range(len(thistuple)):
    print(thistuple[i])


# WHILE LOOP
print("WHILE LOOP")
thistuple = ("apple", "banana", "cherry")
i=0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

print("---------------------------------SETS-------------------------------")

thisset = {"apple",1,2,3,3.4}

for x in thisset:
    print(x)