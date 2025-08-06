class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols=len(img),len(img[0])
        output=[[0] * cols for k in range(rows)]
        for i in range(rows):
            for j in range(cols):
                total,count=0,0
                for r in range(i-1,i+2):
                    for c in range(j-1,j+2):
                        if r<0 or r==rows or c<0 or c==cols:
                            continue 
                        total+=img[r][c]
                        count+=1
                output[i][j]=total//count
        return output        



        