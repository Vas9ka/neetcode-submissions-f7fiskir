# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.answer = 0

        def good(node, curr_max):
            if not node:
                return
            if node.val >= curr_max:
                self.answer += 1
                curr_max = node.val

            left_good = good(node.left, curr_max)
            right_good = good(node.right, curr_max)
        
        good(root, root.val)
        return self.answer

        