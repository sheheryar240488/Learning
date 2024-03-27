
""" SORT """

# Sort List Alphanumerically.
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thisList = ["Apple","Zalando","H&M","Superdry"]
thisList.sort()
print(thisList)

thisList = ["Apple","Zalando","H&M","SuperDry","allure"] # small letter will after capital letters as shown in result.
thisList.sort()
print(thisList)


#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort the list descending:

thislist = ["z", "m", "k", "p", "a"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Reverse the order of the list items:

thislist = ["1", "9", "8", "8"]
thislist.reverse()
print(thislist)