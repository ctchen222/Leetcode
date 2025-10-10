class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        isExist = False
        for i in range(len(matrix)):
            for j in matrix[i]:
                if j == target:
                    isExist = True
                    return isExist
        return False