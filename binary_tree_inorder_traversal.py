class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        traversed = []
        
        curr = root
        while curr is not None or not len(stack) == 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            traversed.append(curr.val)
            curr = curr.right
        
        return traversed
        
