# Profit Analysis

You need to analyze the performance of investments in a stock.

The profit and loss (`pnl`) for each month is represented in an array where each value indicates the profit earned (positive value) or loss incurred (negative value) in that month.

Your task is to find the maximum net profit that can be gained from any contiguous segment of months, with the constraint that the segment cannot exceed a given number of months `k`.

## Function Description

Complete the function `getMaxProfit` with the following parameters:

- `pnl[n]`: monthly profits and losses
- `k`: maximum number of months to consider

## Returns

- `long_int`: the sum of a contiguous subarray of size `k` or less that has the largest sum

## Example

```text
n = 6
pnl = [-3, 4, 3, -2, 2, 5]
k = 4
```

The optimal subarray is `[3, -2, 2, 5]` with a total profit of `8`.
Although `[4, 3, -2, 2, 5]` has a larger sum of `12`, its length exceeds the limit `k = 4`.

So the answer is `8`.

## Constraints

- `1 <= n <= 2 * 10^5`
- `-10^9 <= pnl[i] <= 10^9`
- `1 <= k <= n`

## Input Format For Custom Testing

```text
The first line contains an integer, n, denoting the number of elements in pnl.
Each of the next n lines contains an integer denoting pnl[i].
The last line contains an integer, k.
```

## Sample Case 0

### Sample Input For Custom Testing

```text
7
4
3
-2
9
-4
2
7
6
```

### Sample Output

```text
15
```

### Explanation

We can select the subarray `[3, -2, 9, -4, 2, 7]` with a sum of `15` and size `6`, which is equal to `k`.

## Sample Case 1

### Sample Input For Custom Testing

```text
8
2
5
-7
8
-6
4
1
-9
5
```

### Sample Output

```text
8
```

### Explanation

We can select the subarray `[2, 5, -7, 8]` with a sum of `8` and size `4`, which is less than `k`.
