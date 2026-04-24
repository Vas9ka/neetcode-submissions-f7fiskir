"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        if not root:
            return root
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i + 1 < size:
                    node.next = q[0]
        
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
        
        return root