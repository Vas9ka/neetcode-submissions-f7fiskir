# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = 0
        self.cnt = k
        def dfs(node):
            if not node:
                return 
            left = dfs(node.left)
            self.cnt -= 1
            if self.cnt == 0:
                self.smallest = node.val
                return 
            dfs(node.right)
        dfs(root)
        return self.smallest