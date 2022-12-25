def linearSearchAlgorithm(array,key):
    for i in range(len(array)):
        if array[i] == key  : 
            return 'the index :',i       
    return -1

array = input('Please enter a set: ')
key = input("please enter the key: ")
print("The result: ", linearSearchAlgorithm(array,key))