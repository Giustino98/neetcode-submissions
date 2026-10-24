# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.counter = 0
        self.res = None

        def dfs(node):
            if not node: return

            if dfs(node.left): return True
            self.counter += 1
            if self.counter == k: 
                self.res = node.val
                return True
            if dfs(node.right): return True
        
        dfs(root)
        
        return self.res


