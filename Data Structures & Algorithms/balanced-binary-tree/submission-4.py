# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(root: Optional[TreeNode]) -> int:
            if not root: return 0

            height_left = check_height(root.left)
            height_right = check_height(root.right)

            if height_left == -1 or height_right == -1: return -1

            if abs(height_left - height_right ) > 1: return -1

            return 1 + max(height_left,height_right)
        
        return check_height(root) != -1



            


