# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = TreeNode()
        
        def dfs(node):
            if (node.val >= p.val and node.val <= q.val) or (node.val >= q.val and node.val <= p.val):
                self.res = node
                return
            
            if node.val >= p.val and node.val >= q.val :
                dfs(node.left)
                return
            
            if node.val <= p.val and node.val <= q.val:
                dfs(node.right)
                return
        
        dfs(root)
        return self.res

            
