class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss ="".join(ch.lower() for ch in s if ch.isalnum())
        return True if ss[::-1] == ss else False
        