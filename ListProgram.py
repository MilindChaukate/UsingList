from traceback import print_tb

myList = ['Banana', 'Mango', 'Cherry', 'Apple']
print(myList)

myList.append("Pineapple")
print(myList)

myList.insert(2, "Grapes")
print(myList)

myList[2] = "Strawberry"
print(myList)

mylist2 = ['Papaya', 'Orange', 'Coconut']
myList.extend(mylist2)
print(myList)

for i in myList:
    print(i)

print(myList[4])

print(myList[-4])

print(myList[2:5])

print(myList[:5])

print(myList[5:])

print(myList[-5:-2])

print(myList[-5:])

print(myList[:-2])

x = 0
while x < len(myList):
    print(myList[x])
    x = x + 1

myList.sort()
print(myList)

myList3 = myList.copy()
print(myList3)

myList4 = [10, 20, 30 ,40]
joinList = myList + myList4
print(joinList)

myList.reverse()
print(myList)

joinList.remove(10)
print(joinList)

myList4.clear()
print(myList4)