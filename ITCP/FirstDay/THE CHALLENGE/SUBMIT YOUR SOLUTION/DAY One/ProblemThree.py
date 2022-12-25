
list =[1,2,3,4,5,3]
newList = []
for x in list:
    if x not in newList:
        newList.append(x) 
print("The test list is: ", list)
print("The list without duplicates is: ", newList)

 