# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if not root1 and not root2: return True

            if not root1 or not root2: return False
            if root1.val != root2.val: return False

            return isSameTree(root1.left,root2.left) and isSameTree(root1.right,root2.right)

        if not root: return False #ho fatto dfs ma questo ramo non mi ha mai tornato True

        if not isSameTree(root,subRoot):  #non ho finito dfs, nessun subtree trovato
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else: return True

