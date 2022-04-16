# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getSumBST(root):
            queue = [root]
            sumOfValues = 0
            
            while queue:
                curr = queue.pop()
                if curr is None: continue
                sumOfValues += curr.val
                queue.append(curr.left)
                queue.append(curr.right)
            return sumOfValues
        
        def convertBSTHelper(root, preVal):
            if root is None:
                return
            currVal = preVal + getSumBST(root.right) + root.val
            currNode = TreeNode(currVal)
            currNode.left = convertBSTHelper(root.left, currVal)
            currNode.right = convertBSTHelper(root.right, preVal)
            return currNode
        
        return convertBSTHelper(root, 0)

