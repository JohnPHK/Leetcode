class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
        
        return root
        
