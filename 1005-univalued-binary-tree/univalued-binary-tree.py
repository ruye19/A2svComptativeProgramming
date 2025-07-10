# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        output=[]
        visited=set([root])
        queue=deque([root])
        while queue:
            node=queue.popleft() 
            output.append(node.val)
            for i in (node.left,node.right):
                if i and i not in visited:
                    visited.add(i)
                    queue.append(i)
        return len(set(output))==1
