# Brute force
# def StockPicker(arr):
#   result = -1
#   n = len(arr)
#   for i in range(n - 1):
#     for j in range(i + 1, n):
#       profit = arr[j] - arr[i]
#       if profit >= 0 and profit > result:
#         result = profit
#   return result

# O(n) solution
def StockPicker(arr):
    if len(arr) < 2:
        return 0
    
    max_profit = -1
    min_price = arr[0]
    for price in arr[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


assert StockPicker([10, 12, 4, 5, 9]) == 5
assert StockPicker([14, 20, 4, 12, 5, 11]) == 8
assert StockPicker([10, 7, 5, 8, 11, 9]) == 6
