https://coderbyte.com/editor/Stock%20Picker:Python3
Difficulty: Medium

## Critical thinking
This is a classic array manipulation and greedy problem. The brute force solution is to check all possible pairs of buy and sell days, but this results in O(n^2) time complexity. A more efficient approach is to iterate through the array while keeping track of the minimum price seen so far and the maximum profit that can be achieved. For each price, calculate the profit if you were to sell at that price, and update the maximum profit accordingly. This allows for an O(n) time complexity solution.

The tricky part is ensuring you only buy before you sell, and handling cases where no profit is possible (e.g., prices are always decreasing). In such cases, the function should return -1 or 0, depending on the problem statement.

## Complexity
### Time complexity: **O(N)**
N is the number of days (length of the prices array). We only traverse the array once, updating the minimum price and maximum profit as we go.
### Space complexity: **O(1)**
Only a few variables are used to keep track of the minimum price and maximum profit, so space usage is constant.
