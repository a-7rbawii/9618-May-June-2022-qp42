global StackData
global StackPointer

def OutputStack():
    global StackData
    global StackPointer
    print("Stack data:")
    for i in range(10):
        print(StackData[i])
    print("Pointer: {}".format(StackPointer))

def pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        returnvalue = StackData[StackPointer]
        return returnvalue

def Push(item):
    global StackData, StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = item
        StackPointer = StackPointer + 1
        return True

StackData = [0 for i in range(10)]
StackPointer = 0

for i in range(11):
    item = int(input("Enter number: "))
    if Push(item) == True:
        print("Pushed")
    else:
        print("Stack is full")
OutputStack()

for i in range(2):
    removed = pop()
    print("{} is popped".format(removed))
OutputStack()
