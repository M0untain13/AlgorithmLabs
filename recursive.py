import random


def Main():
    FindDigitCountTask()
    print()
    MethodHoareTask()


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
    if(number != 0):
        return count + FindDigitCount(number, m)
    
    return count


def GenerateNumber(n: int) -> int:
    return random.randint(10**(n-1), 10**n - 1)


def MethodHoareTask():
    print("Задание 2")
    array = [random.randint(0, 999) for _ in range(100)]
    print(array)
    QuickSort(array, 0, len(array) - 1)
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


if __name__ == "__main__":
    Main()