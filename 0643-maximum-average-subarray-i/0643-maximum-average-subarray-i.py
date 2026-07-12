class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        cur_num = 0

        for i in range(k):
            cur_num += nums[i]

        max_avg = cur_num / float(k)

        for i in range(k, n):
            cur_num += nums[i]
            cur_num -= nums[i-k]
            
            avg = cur_num / float(k)
        
            max_avg = max(max_avg, avg)

        return max_avg