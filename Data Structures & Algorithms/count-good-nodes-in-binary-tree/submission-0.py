# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def countGoodNodes(root : Optional[TreeNode], maxn: int) -> None:
            if not root: return
            if root.val >= maxn:
                self.counter += 1
                maxn = root.val
            countGoodNodes(root.left, maxn)
            countGoodNodes(root.right, maxn)

        countGoodNodes(root, root.val)
        return self.counter


