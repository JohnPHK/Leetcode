# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:


    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.traverse_left(root)
    
    def traverse_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top_node = self.stack.pop()
        
        if top_node.right:
            self.traverse_left(top_node.right)
        return top_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
