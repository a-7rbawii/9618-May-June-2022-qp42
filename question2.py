import random

def outputarray(array):
    for i in range(10):
        for j in range(10):
            print(array[i][j]," ",end= '')
        print("")

def BinarySearch(array, lower, upper, item):
    if upper >= lower:
        mid = (lower + (upper-1))//2
        if array[0][mid] == item:
            return mid
        else:
            if array[0][mid] > item:
                return BinarySearch(array, lower, mid - 1, item)
            else:
                return BinarySearch(array, mid + 1, upper, item)
    return -1

array = [[0]*10 for i in range(10)]

for i in range(10):
    for j in range(10):
        array[i][j] = random.randint(1,100)

print("Before:")
outputarray(array)

arrayLength = 10
for x in range(arrayLength):
    for y in range(arrayLength - 1):
        for z in range(arrayLength - y - 1):
            if array[x][z] > array[x][z+1]:
                temp = array[x][z]
                array[x][z] = array[x][z+1]
                array[x][z+1] = temp

print("After:")
outputarray(array)

for i in range(2):
    item = int(input("Input item to be searched: "))
    result = BinarySearch(array, 0, len(array), item)

    if result == -1:
        print("Item not found")
    else:
        print("found at {}".format(result))