from func_laba2 import funSum

def funMain():
    nums = []
    
    print("Enter the number of array elements: ")
    n = int(input()) 

    print("Enter each element of the array: ")
    for i in range(n):
        item = int(input())
        nums.append(item)

    print("Enter the target: ")
    target = int(input())

    res = funSum(nums, target)

    return res

print(funMain())