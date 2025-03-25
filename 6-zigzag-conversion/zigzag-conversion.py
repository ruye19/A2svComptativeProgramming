class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row].append(char)
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        
        result = []
        for row in rows:
            result.extend(row)
        return ''.join(result)