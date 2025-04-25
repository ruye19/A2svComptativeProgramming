# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def gotsum(root,targetsum):
            if not root: return False

            if not root.right and not root.left:
                return targetsum==root.val

            return gotsum(root.left, targetsum-root.val) or (gotsum(root.right, targetsum-root.val) ) 
        return gotsum(root,targetSum)
            