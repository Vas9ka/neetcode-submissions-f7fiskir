# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, d):
            if not node:
                return 0,0
            
            left_d, left_height = dfs(node.left, d)
            right_d, right_height = dfs(node.right, d)
            current_d = left_height + right_height
            d = max(left_d, right_d, current_d)

            return d, max(left_height, right_height) + 1
        

        d, _ = dfs(root, 0)
        return d