"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        elif len(root.children) == 0:
            return 1
        else:
            return max([self.maxDepth(node) for node in root.children]) + 1