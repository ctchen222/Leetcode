class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        while True:
            if count == k:
                break
            number = nums.pop()
            nums.insert(0, number)
            
            count += 1