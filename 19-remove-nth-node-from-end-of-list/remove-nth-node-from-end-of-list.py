class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode(0, head)
        

        curr = head
        while curr:
            length += 1
            curr = curr.next
        k = (length - n) + 1
        
        count = 0
        prev = dummy
        curr = head
        while curr:
            count += 1
            if count == k:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next 
        return dummy.next
