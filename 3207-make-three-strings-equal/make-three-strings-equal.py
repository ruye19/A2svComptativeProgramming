class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        mini=min(len(s1),len(s2),len(s3))
        total=len(s1)+len(s2)+len(s3)

        if not s1[0]==s2[0]==s3[0]: return -1

        for i in range(mini):
            if s1[i]==s2[i]==s3[i]:
                total-=3
            else:
                break
              
        return total       
                        

        