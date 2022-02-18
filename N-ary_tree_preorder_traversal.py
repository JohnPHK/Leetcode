# Recursion version
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if root is None:
                return 
            
            res.append(root.val)
            for child in root.children:
                helper(child)
        
        
        helper(root)
        
        return res

# Iterative version
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res, stack = [], [root]
        if root is None:
            return []
        
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack = stack + curr.children[::-1]
        
        
        return res