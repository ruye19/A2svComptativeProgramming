class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output=[]
        m,n=len(matrix),len(matrix[0])
        top,down,right,left =0,m,n,0
        while top<down and left<right:
            for i  in range(left,right):
                output.append(matrix[top][i])
            top+=1
           
            for i  in range(top,down):
                output.append(matrix[i][right-1])
            right-=1    
            
            if not(left<right and top<down):
                break
            
            for i  in range(right-1,left-1,-1):
                output.append(matrix[down-1][i])
            down-=1    
            
            for i  in range(down-1,top-1,-1):
                output.append(matrix[i][left])
            left+=1
        return output 

            


                

        