class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: False
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // cols, mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False