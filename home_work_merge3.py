def merge(arr, l, m, r, s, counter):
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
    
    i, j = 0, 0
    counter.append(0)
    
    while (i + j) != (n1 + n2):
        x = arr[l+i] + arr[r-j-1]
        if x < s:
            i += 1
        elif x > s:
            j += 1
        else:
            counter[-1] += 1
            i += 1
    
    return counter


def merge_sort(arr, l, r, s, counter=[]):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(arr, l, m, s)
        merge_sort(arr, m + 1, r, s)
        merge(arr, l, m, r, s, counter)
    return counter

arr = [5,4,3,2,1]
print(arr)
print(merge_sort(arr, 0, len(arr) - 1, 7)[-1])
print(arr)