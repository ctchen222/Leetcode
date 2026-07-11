class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        for num in nums:
			if num not in frequency:
				frequency[num] = 1
			else:
				frequency[num] = frequency[num] + 1
        sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return [num for num, count in sorted_items[:k]]