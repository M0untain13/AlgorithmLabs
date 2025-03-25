import random

def Main():
    FindDigitCountTask()
    print()
    MethodHoareTask()
    print()
    MethodHoareRecursive()
    print()
    NodTask()
    print()

# =====  Задание 1  =====
def FindDigitCountTask() -> None:
    print("Задание 1")
    number = GenerateNumber(600)
    m = 5
    count = FindDigitCount(number, m)
    print(f"Number: {number}\nCount: {count}")

def FindDigitCount(number, m) -> int:
    digit = number % 10
    count = 0
    if (m == digit):
        count += 1
    number = number//10
    if(number == 0):
        return count 
    else:
        return count + FindDigitCount(number, m)

def GenerateNumber(n: int) -> int:
    return random.randint(10**(n-1), 10**n - 1)
# =====             =====

# ===== Задание 2.1 =====
def MethodHoareTask():
    print("Задание 2.1")
    array = [random.randint(0, 100) for _ in range(20)]
    print("Array")
    print(array)
    QuickSort(array, 0, len(array) - 1)
    print("Sorted")
    print(array)

def QuickSort(arr, low, high):
    if low < high:
        # pi - это индекс опорного элемента, arr[pi] теперь находится на правильном месте
        pi = Partition(arr, low, high)
        # отдельно сортируем элементы до и после разделения
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)

def Partition(arr: list[int], low: int, high: int) -> int:
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
# =====             =====

# ===== Задание 2.2 =====
def MethodHoareRecursive():
    print("Задание 2.2")
    array = [random.randint(0, 100) for _ in range(20)]
    print("Array")
    print(array)
    array = QuicksortRecursive(array)
    print("Sorted")
    print(array)

def QuicksortRecursive(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    def quicksort_tail_recursive(low, high):
        while low < high:
            pi = partition(low, high)
            quicksort_tail_recursive(low, pi - 1)
            low = pi + 1
    quicksort_tail_recursive(0, len(arr) - 1)
    return arr
# =====             =====

# =====  Задание 3  =====
def NodTask():
    print("Задание 3")
    # 13*517=6721 13*812=10556
    print("Метод 1:", gcd1(6721, 10556)) 
    print("Метод 2:", gcd2(6721, 10556))

def gcd1(m, n):
    if m == 0:
        return n
    elif m > n:
        return gcd1(n, m)
    else:
        return gcd1(m, n - m)

def gcd2(m, n):
    if m == 0:
        return n
    else:
        return gcd2(n%m, m)
# =====             =====

if __name__ == "__main__":
    Main()