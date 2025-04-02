class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        charTracker=set()
        longest=0
        l=0
        for r in range (len(s)):
            while s[r] in charTracker:
                charTracker.remove(s[l])
                l+=1
            charTracker.add(s[r])
            longest=max(longest,r-l+1)
        return longest                              