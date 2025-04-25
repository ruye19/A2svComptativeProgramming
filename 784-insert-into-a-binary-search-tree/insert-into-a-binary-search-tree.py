# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertion(node,val):
            if not node: return TreeNode(val)
            if node.val< val:
                node.right= insertion(node.right,val)
            elif node.val>val:
                node.left=insertion(node.left ,val)
            return node    
        return insertion(root,val)                

        