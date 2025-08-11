class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first="qwertyuiopQWERTYUIOP"
        second="asdfghjklASDFGHJKL"
        third="zxcvbnmZXCVBNM"
        output=[]
        for word in words:
            s=""
            for i in word:
                if i in first:
                    s+="f"
                if i in second:
                    s+="s"
                if i in third:
                    s+="t"
            print(s)        
            if len(set(s))==1:
                output.append(word)
        return output         






        