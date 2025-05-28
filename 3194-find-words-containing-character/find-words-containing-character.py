class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        array_of_indice=[]
        for i in range(len(words)):
            if x in words[i]:
                array_of_indice.append(i)
        return array_of_indice        
