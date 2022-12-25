#Input arrays
arrayOne = [0 , 2 , 4 , 6 , 8]
arrayTwo = [1 , 3 , 5 , 7]
#Merge and sort the arrays in one array
arrayMerged = arrayOne+ arrayTwo
arrayMergedAndSorted= sorted(arrayMerged)
#Returning the arrays in same lenght as initiative one, with numbers ordered
arrayOneReturned = []
arrayTwoReturned = []
for number in arrayMergedAndSorted:
    if len(arrayOneReturned)< len(arrayOne):
        arrayOneReturned.append(number)
    else:
        arrayTwoReturned.append(number)

print("The first input array: ", arrayOne)
print("The second input array: ", arrayTwo)
print("Output______________________________________")
print("The first returned array: ", arrayOneReturned)
print("The second returned array: ", arrayTwoReturned)

