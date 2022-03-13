"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        _dict = {}
        
        
        curr = head
        while curr:
            _dict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                _dict[curr].next  = _dict[curr.next]
            else:
                _dict[curr].next = None
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                _dict[curr].random = _dict[curr.random]
            else:
                _dict[curr].random = None
            curr = curr.next
            
        return _dict[head]
        
        
