# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def travers(root,curPath):
           
            if not root.right and not root.left:
               result.append("->".join(curPath))
               return 
            if root.left:
                travers(root.left,curPath + [str(root.left.val)])    
            if root.right:
                travers(root.right,curPath + [str(root.right.val)])    
        result=[]
        travers(root,[str(root.val)]) 
        return result       
                  
                 