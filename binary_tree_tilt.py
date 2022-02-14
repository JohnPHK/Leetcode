# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt_val = 0
        def sumBT(node):
            
            if not node:
                return 0
            
            left_sum = sumBT(node.left)
            right_sum = sumBT(node.right)
            self.tilt_val += abs(left_sum - right_sum)
            
            return left_sum + right_sum + node.val
            
        sumBT(root)
        
        return self.tilt_val