# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def searchtree(root,val):
            if not root: return None
            if val > root.val:
                return  searchtree(root.right,val)
            elif val<root.val:    
                return  searchtree(root.left,val)
            elif val==root.val:
                return root
               
        return searchtree(root,val)            




        
        