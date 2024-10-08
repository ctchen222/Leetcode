class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        currentSum = numbers[left] + numbers[right]
        while currentSum != target:
            if currentSum > target:
                right -= 1
            else:
                left += 1
            currentSum = numbers[left] + numbers[right]

        return [left+1, right+1]
            
            