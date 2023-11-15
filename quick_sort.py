from random import randint


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivod = arr[randint(0, len(arr) - 1)]
    less = []
    equal = []
    grater = []

    for x in arr:
        if x < pivod:
            less.append(x)
        elif x > pivod:
            grater.append(x)
        else:
            equal.append(x)

    quick_sort(less)
    quick_sort(grater)
    return less + equal + grater


if __name__ == "__main__":
    from pprint import pprint
    from random import randint

    arr = [randint(-100, 100) for _ in range(20)]
    print(arr)
    arr = quick_sort(arr)
    print(arr)
