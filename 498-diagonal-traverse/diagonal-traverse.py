class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n,m=len(mat),len(mat[0])
        output=[]
        sum_collection=defaultdict(list)
        for i in range(n):
            for j in range(m):
                sum_collection[i+j].append(mat[i][j])        
        for key,value in sum_collection.items():
            if key%2==0:
                output.extend(value[::-1])
            else:
                output.extend(value)  
        return output

