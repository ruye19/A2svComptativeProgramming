class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.result = [[0] * (cols + 1)  for i in range(rows + 1)]

        for r in range(rows):
            prefix = 0 
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.result[r][c + 1]
                self.result[r + 1][c + 1] = prefix + above 
                
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1 , r2, c2 = r1 + 1, c1 + 1,r2 + 1,c2 + 1
        br = self.result[r2][c2]
        above = self.result[r1 - 1][c2]
        left = self.result[r2][c1 - 1]  
        topl = self.result[r1 - 1][c1 - 1]
        return br - above - left + topl


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)