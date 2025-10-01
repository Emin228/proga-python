from labs1 import funSum


mas = []

print("Enter the number of array elements: ")
n = int(input())

for i in range(n):
    item = int(input())
    mas.append(item)

print("Enter the target: ")
target = int(input())

res = funSum(mas, target)

print(res)