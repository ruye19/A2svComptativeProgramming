class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search_array = [] 
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
               search_array.append(matrix[i][j])
        left, right = 0, len(search_array) - 1
        while left <= right:
            mid = (left + right) // 2
            if search_array[mid] < target:
                left = mid + 1
            elif search_array[mid] == target: 
                return True 
            else:
                right = mid - 1
        return False