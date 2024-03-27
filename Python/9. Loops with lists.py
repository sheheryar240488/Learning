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

