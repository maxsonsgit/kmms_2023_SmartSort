def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1 + [float("inf")]
    R = [0] * n2 + [float("inf")]

    for i in range(n1):
        L[i] = arr[l + i]
    for i in range(n2):
        R[i] = arr[m + 1 + i]

    i, j, k = 0, 0, l
    while k <= r:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


if __name__ == "__main__":
    from pprint import pprint
    from random import randint

    arr = [randint(-100, 100) for _ in range(5)]
    print(arr)
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)
