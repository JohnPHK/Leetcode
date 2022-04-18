# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recusrive version
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def inorder_traversal(root):
            if root is not None:
                inorder_traversal(root.left)
                if self.k == 1: 
                    self.kth_smallest = root.val
                self.k -= 1
                inorder_traversal(root.right)
        
        inorder_traversal(root)
        return self.kth_smallest

# Iterative version
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if k == 1: return root.val
                k -= 1
                current = current.right
            else:
                break

                
