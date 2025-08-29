class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1        
        while start < end:
            if s[start] != s[end]:
                skipl, skipr = s[start + 1:end + 1], s[start:end]
                return (skipl == skipl[::-1] or skipr == skipr[::-1])
            start += 1
            end -= 1

        return True         