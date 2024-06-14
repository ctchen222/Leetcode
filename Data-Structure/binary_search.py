def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        if arr[mid] < target:
            left = mid + 1
        if arr[mid] == target:
            return mid
    return -1


if __name__ == '__main__':
    my_list = [2, 4, 7, 12, 15, 21, 30, 34, 42]
    target_number = 3
    result = binarySearch(my_list, target_number)

    if result != -1:
        print(f"目標數字 {target_number} 存在於數列中，索引位置為 {result}")
    else:
        print(f"目標數字 {target_number} 不存在於數列中")
