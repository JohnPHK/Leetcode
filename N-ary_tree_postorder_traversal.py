class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res, stack = [], [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            for child in curr.children:
                stack.append(child)
        return res[::-1]
