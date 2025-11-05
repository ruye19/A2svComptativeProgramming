class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    res.append((i,j))
        for row,col in res:            
            matrix[row] = [0] * cols
            for ro in matrix:
                ro[col] = 0            
        return matrix                 

