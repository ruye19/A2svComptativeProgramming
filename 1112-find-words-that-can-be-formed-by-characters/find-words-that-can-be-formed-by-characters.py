from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        out_count = 0
        chars_count = Counter(chars)

        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= chars_count[c] for c in word_count):
                out_count += len(word)
    
        return out_count
