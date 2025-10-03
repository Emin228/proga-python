from func_laba2 import funSum

def funMain():
    mas = []
    n =0
        
    print("Enter the number of array elements: ")
    n = int(input()) 

    print("Enter each element of the array: ")
    for i in range(n):
        item = int(input())
        mas.append(item)

    print("Enter the target: ")
    target = int(input())

    res = funSum(mas, target)

    return res

print(funMain())