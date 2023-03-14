# time and space complexity analysis
#
# example

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

Time сложность функции insertion_sort(arr) равна O(n^2), где n — длина входного списка
Space сложность функции insertion_sort(arr) равна O(1) Функция изменяет входной список на месте, не создавая никаких новых структур данных.

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

time O(log n) почему???
space O(1) почему ???



def matrix_multiply(matrix1, matrix2):
    n1, m1 = len(matrix1), len(matrix1[0])
    n2, m2 = len(matrix2), len(matrix2[0])

    if m1 != n2:
        raise ValueError("Invalid dimensions")

    result = [[0] * m2 for _ in range(n1)]

    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


ИЗОБРАЗИТЬ В ВИДЕ БЛОК-СХЕМЫ

if door is closed:
    if door is locked:
        unlock_door()
    open_door()
advance()