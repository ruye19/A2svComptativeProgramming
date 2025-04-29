# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def summ(root,parent,grandParent):
            if not root: return 0
            total=0
            if grandParent and  grandParent.val %2==0:
                total+=root.val
            temp =parent
            parent=root
            grandParent=temp
            return  total + summ(root.left, parent,grandParent) + summ(root.right,parent,grandParent)

        return summ(root,None,None)   