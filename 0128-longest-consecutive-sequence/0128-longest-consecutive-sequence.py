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

# Time Complexty: O(n)
# -> Nested While loop inside for loop runs at most n times in total. When it happened, rest of the numbers will be skipped in the for loop. -> total time complexity is O(n)
# Space Complexity: O(n)

sol = Solution()

assert(sol.longestConsecutive([100,4,200,1,3,2]) == 4)
assert(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9)
assert(sol.longestConsecutive([1,0,1,2]) == 3)
