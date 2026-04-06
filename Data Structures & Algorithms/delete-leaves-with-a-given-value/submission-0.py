# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node, parent):
            if not node:
                return
            dfs(node.left, node)
            dfs(node.right, node)
            if not node.left and not node.right and node.val == target:  
                    if parent and parent.left == node:
                        parent.left = None
                    if parent and parent.right == node:
                        parent.right = None
                        
        dummy = TreeNode(left=root)
        dfs(dummy, None)
        return dummy.left 