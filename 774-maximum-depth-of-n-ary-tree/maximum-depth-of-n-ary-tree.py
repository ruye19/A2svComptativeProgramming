from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                for child in node.children or []:
                    queue.append(child)
            depth += 1
        
        return depth
