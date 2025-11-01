class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first="qwertyuiopQWERTYUIOP"
        second="asdfghjklASDFGHJKL"
        third="zxcvbnmZXCVBNM"
        rows = [first, second, third]
        rowNum = 0
        lookup = {}
        output =[]
        for row in rows:
            for char in row:
                lookup[char] = rowNum
            rowNum += 1    
        for word in words:
            for c in range(len(word) - 1):
                if lookup[word[c]] != lookup[word[c + 1]]:
                    break
            else:
                output.append(word)
        return output        


                                                                                                                                                                                                                                 
                 






        