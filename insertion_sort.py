def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            j = i
            while (arr[j-1] > arr[j] and j > 0):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1


if __name__ == "__main__":
    from pprint import pprint
    from random import randint

    arr = [randint(-100, 100) for _ in range(5)]
    #arr = [-4, -20, -70, 93, -62]
    print(arr)
    insertion_sort(arr)
    print(arr)

