class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, cols = len(matrix), len(matrix[0])
        transpose = [[0] * row for _ in range(cols) ]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                transpose[c][r] = matrix[r][c]
        return transpose        
        