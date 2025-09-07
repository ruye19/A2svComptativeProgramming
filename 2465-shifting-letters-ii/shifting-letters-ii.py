class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)  
        for l, r, shift in shifts:
            prefix_sum[r + 1] += 1 if shift else -1
            prefix_sum[l] -= 1 if shift else -1
        d = 0 
        result = [ord(i) - ord("a") for i in s] 
        for k in reversed(range(len(prefix_sum))):
            d += prefix_sum[k]
            result[k - 1] = (result[k - 1] + d) % 26 

        s = [chr(ord("a") + f) for f in result]
        return "".join(s)


            
