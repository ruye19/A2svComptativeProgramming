class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        count = 0 
        # maximum = 0
        k = 0
        
        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[k])
                k += 1
            substring.add(s[i])
            count  = max(count, i - k + 1)
        return count        

