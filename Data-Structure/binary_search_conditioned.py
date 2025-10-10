# Contioned binary search
# Given a sorted array of integers and a target value,
# Given: [False, False, False, True, True, True]
# Find the first occurrence of the target value (True)

def binarySearchConditioned(arr, target) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        if arr[mid] >= target:
            right = mid
    return left


if __name__ == '__main__':
    my_list = [False, True, True, True, True, True]
    result = binarySearchConditioned(my_list, True)

    if result != -1:
        print(f"目標值 True 存在於數列中，索引位置為 {result}")
    else:
        print(f"目標值 True 不存在於數列中")
