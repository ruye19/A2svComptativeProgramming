class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
       
        broken = len(brokenLetters)
        count = len(text.split())
        for word in text.split():
            for ch in brokenLetters:
                if ch in word:
                    count -= 1
                    break
        return count        
            