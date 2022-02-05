class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr = l1
        l2_ptr = l2
        holder = ListNode()
        itr_ptr = holder
        carry = 0
        
        while l1_ptr is not None and l2_ptr is not None:
            new_val = l1_ptr.val + l2_ptr.val + carry
            if new_val >= 10:
                itr_ptr.next = ListNode(new_val - 10)
                carry = 1
            else:
                itr_ptr.next = ListNode(new_val)
                carry = 0
            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next
            itr_ptr = itr_ptr.next
        
        if l2_ptr is not None:
            while l2_ptr is not None:
                if l2_ptr.val + carry >= 10:
                    itr_ptr.next = ListNode(l2_ptr.val + carry - 10)
                    carry = 1
                else:
                    itr_ptr.next = ListNode(l2_ptr.val + carry)
                    carry = 0
                l2_ptr = l2_ptr.next
                itr_ptr = itr_ptr.next
        
        elif l1_ptr is not None:
            while l1_ptr is not None:
                if l1_ptr.val + carry >= 10:
                    itr_ptr.next = ListNode(l1_ptr.val + carry - 10)
                    carry = 1
                else:
                    itr_ptr.next = ListNode(l1_ptr.val + carry)
                    carry = 0
                l1_ptr = l1_ptr.next
                itr_ptr = itr_ptr.next
        
        if carry == 1:
            itr_ptr.next = ListNode(1)
        
        return holder.next
