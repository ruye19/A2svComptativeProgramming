class Solution:
    def isThree(self, n: int) -> bool:
        count =0
        if n==1:
            return False
        for i in range (1,n+1):
            if n%i==0:
                count+=1
                
        return count==3         

        