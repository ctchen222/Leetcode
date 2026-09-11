class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * (n + 1)
        suffix = [1] * (n + 1)

        # prefix
        for i in range(1, n+1):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # suffix
        for j in range(n-1, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j]

        result = [prefix[i] * suffix[i+1] for i in range(n)]

        return result

# Input: nums = [1,2,3,4]
# prefix = [1, 1, 2, 6, 24]
# suffix = [24, 24, 12, 4, 1]

# Brute force - pseudo code
# for i = 1...n
#     for j = 1...n
#         tmp = 1
#         if j != i: tmp *= nums[j]
#     result.append(tmp)
# return result

# Brute force Solution
# n = len(nums)
# result = [0] * n
# for i in range(n):
#     for j in range(n):
#         tmp = 1
#         if j != i:
#             tmp *= num[j]
#     result[i] = tmp
# return result