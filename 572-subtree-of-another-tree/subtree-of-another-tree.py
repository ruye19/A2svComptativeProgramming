# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helperSametree(root,subRoot):
           if not root and not subRoot:
            return True
           if (not root and subRoot ) or (not subRoot and root):
            return False
           if root.val != subRoot.val:
            return False
           if root.val== subRoot.val:
             return helperSametree(root.left,subRoot.left ) and helperSametree(root.right,subRoot.right)
                     
        def issub(root):
            if not root :
                return False
            if helperSametree(root,subRoot):
                return True 
            return issub(root.left ) or issub(root.right)
        return issub(root)                            
    
           
