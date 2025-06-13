class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(numRows-1):
            t=[0]+ans[-1]+[0]
            row=[]
            for j in range(len(ans[-1])+1):
                row.append(t[j]+t[j+1])
            ans.append(row)
        return ans        

