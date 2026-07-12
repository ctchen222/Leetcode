class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
            # beginning of consecutive sequence
                consecutive = 1
                next_num = num + 1
                while next_num in s:
                    consecutive += 1
                    next_num += 1
                longest = max(longest, consecutive)
        return longest