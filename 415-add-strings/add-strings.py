class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i ,j = len(num1)-1,len(num2)-1
        carry=0
        result=[]
        while i>=0 or j>=0 or carry:
            curi=int(num1[i]) if i >= 0 else 0
            curj=int(num2[j])  if j >= 0 else 0

            curSum=curi+curj+carry
            result.append(str(curSum % 10))
            carry=curSum // 10

            i-=1
            j-=1

        if carry:
            result.append(str(carry))    
        return "".join(reversed(result))    
