# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result=[]
        q=deque([root])
        while q:
            row_max=q[0].val
            for _ in range(len(q)):
                node= q.popleft()
                row_max=max(node.val,row_max)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(row_max)
        return result 
       

           


           
        