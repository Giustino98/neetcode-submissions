# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root: queue.append(root)
        res = []

        while queue:
            n_nodes = len(queue)
            level_nodes = []
            for _ in range(n_nodes):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(level_nodes)
        
        return res