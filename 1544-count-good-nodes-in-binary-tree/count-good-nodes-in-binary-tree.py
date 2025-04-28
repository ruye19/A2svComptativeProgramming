# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
     
        def good(root,maxValue):            
            if not root: return 0
            current_count= 1 if root.val>=maxValue else 0 
            largest=max(maxValue,root.val)
            return current_count + good(root.left,largest) + good(root.right,largest)
            
        return good(root,root.val)    

