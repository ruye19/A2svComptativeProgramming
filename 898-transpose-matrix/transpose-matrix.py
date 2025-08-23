class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, cols = len(matrix), len(matrix[0])
        transpose = [[0] * row for _ in range(cols) ]
        for r in range(row):
            for c in range(cols):
                transpose[c][r] = matrix[r][c]
        return transpose        
        