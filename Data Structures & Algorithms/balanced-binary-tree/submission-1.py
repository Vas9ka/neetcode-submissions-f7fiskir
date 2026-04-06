# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def check(node):
            if not node:
                return 0
            
            left_h  = check(node.left)
            right_h = check(node.right)
            
            balanced = abs(left_h - right_h) <= 1

            if not balanced:
                self.balanced = False

            return max(left_h, right_h) + 1
        check(root)
        return self.balanced

