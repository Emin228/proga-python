
def funSum(arr, target):
    if type(arr) != list or len(arr) <2:
        return 'Массив отсутсвует, пуст или слишком мал'
    if type(target) != int:
        return "Target нераспознан"
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                return [i, j]
    return 'Отсутсвует комбинация элементов подходящих условию'
            
