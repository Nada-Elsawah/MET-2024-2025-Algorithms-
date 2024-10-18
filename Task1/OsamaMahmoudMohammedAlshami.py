def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(f"\nIteration {i+1}:")
        print(f"Subarray being sorted: {arr[i:]}")
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            print(f"Comparing {arr[j]} with {arr[min_index]} (current minimum)")

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Swapping {arr[min_index]} with {arr[i]}")
        print(f"Array after iteration {i+1}: {arr}")

arr = [55, 34, 22, 78, 13]
print("Original array:", arr)
selection_sort(arr)
print("\nSorted array:", arr)
