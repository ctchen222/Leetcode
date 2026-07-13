class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = self.find_boundary(nums, target)
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

# https://www.youtube.com/watch?v=9nmrkG6QtpQ&list=PLKYEe2WisBTGq9T0wPulXz1otUsVeOGey&index=8
# conditional 部分有講解怎麼找pivot(boundary)
    def find_boundary(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
        if pivot == 0:
            l, r = 0, len(nums) - 1
        elif target <= nums[pivot - 1] and target >= nums[0]:
            l, r = 0, l - 1
        else:
            l, r = l, len(nums) - 1

        return l, r