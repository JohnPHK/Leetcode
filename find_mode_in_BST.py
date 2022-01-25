# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findModeHelper(self, root: Optional[TreeNode], d: Dict) -> (List[int], int):   
        if root == None:
            return
        
        self.findModeHelper(root.left, d)
        self.findModeHelper(root.right, d)
        
        
        
        if root.val in d:
            d[root.val] +=1
        else:
            d[root.val] = 1
        
        
        return d
                        
            
            
            
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        _dict = self.findModeHelper(root, {})
        mode = []
        
        often = 0
        for n in _dict:
            if _dict[n] > often:
                often = _dict[n]
                mode = [n]
            elif _dict[n] == often:
                mode.append(n)
                
        
        return mode
