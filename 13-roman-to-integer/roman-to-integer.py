class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        total=0
        prev_value=0
        for char in reversed(s):
            curr=roman_map[char]
            if curr < prev_value:
                total-=curr
            else:
                total+=curr
            prev_value=curr
        return total                        