# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateSubTree(node: Optional[TreeNode], minimum: int, maximum: int) -> bool:
            if not node: return True
            if node.val <= minimum or node.val >= maximum: return False
            return validateSubTree(node.left, minimum, node.val) and validateSubTree(node.right, node.val, maximum)
        
        return validateSubTree(root, float('-inf'), float('inf'))