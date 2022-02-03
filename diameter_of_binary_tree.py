# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(root):
            if root:
                L = dfs(root.left)
                R = dfs(root.right)
                max_depth = max(L, R) + 1
                self.diameter = max(L+R, self.diameter)
                return max_depth
            else:
                return 0
        
        dfs(root)
        return self.diameter