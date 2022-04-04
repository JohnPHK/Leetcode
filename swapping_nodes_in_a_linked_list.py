# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLength = 0
        curr = head
        front = None
        end = None
        
        while curr:
            listLength += 1
            if end:
                end = end.next
            if listLength == k:
                front = curr
                end = head
            curr = curr.next
        
        front.val, end.val = end.val, front.val
        
        return head
                    