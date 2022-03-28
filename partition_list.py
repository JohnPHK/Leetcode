# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        gtoeDummy = ListNode() # gtoe = greater than or equal
        smallerDummy = ListNode()
        gtoePtr = gtoeDummy
        smallerPtr = smallerDummy
        
        curr = head
        while curr:
            if curr.val < x:
                smallerPtr.next = curr
                smallerPtr = smallerPtr.next
            else:
                gtoePtr.next = curr
                gtoePtr = gtoePtr.next
            curr = curr.next
        
        smallerPtr.next = gtoeDummy.next
        gtoePtr.next = None
        return smallerDummy.next
