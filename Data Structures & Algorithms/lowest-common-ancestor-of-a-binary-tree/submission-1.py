# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find(node, p, q):
            if not node:
                return False
            
            if node == p or node == q:
                return True
            
            return find(node.left, p, q) or find(node.right, p, q)


        def dfs(node, p, q):
            if not node:
                return None
            if node == p or node == q:
                return node
            
            if find(node.left, p, q) and find(node.right, p, q):
                return node
            
            elif find(node.left, p, q):
                return dfs(node.left, p, q)
            
            if find(node.right, p, q):
                return dfs(node.right, p, q)

        return dfs(root, p, q)            
            
