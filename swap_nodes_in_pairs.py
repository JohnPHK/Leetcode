# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = ListNode()
        prev = dummy
        prev.next = curr
        
        while curr and curr.next:
            nex = curr.next
            prev.next = nex
            curr.next = nex.next
            nex.next = curr

            prev = curr
            curr = prev.next
            
            
        return dummy.next
    