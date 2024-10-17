def selection_sort(arr):
    for i in range(0,len(arr) - 1):
        k = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i] #swap


arr = [3, 7, 6, 1, 2, 5]
selection_sort(arr)
print(arr)