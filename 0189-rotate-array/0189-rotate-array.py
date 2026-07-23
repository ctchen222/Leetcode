class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        while True:
            if count == k:
                break
            number = nums.pop()
            nums.insert(0, number)
            
            count += 1