# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def find_d(node):
            if not node:
                return 0
            left = find_d(node.left)
            right  = find_d(node.right)
            
            self.max_d = max(left + right, self.max_d)

            return max(left, right) + 1
        find_d(root)
        return self.max_d
