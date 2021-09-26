def binary_search(array, element):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == element:
            if middle > 0 and array[middle - 1] == element:
                while array[middle] == element:
                    middle = middle - 1
                return middle + 1
            else:
                return middle
        elif array[middle] > element:
            end = middle - 1
        elif array[middle] < element:
            start = middle + 1


arr = [1, 4, 4, 4, 6, 10, 10, 10, 14, 18, 22, 22, 22, 22]

# print(binary_search(arr, 22))
