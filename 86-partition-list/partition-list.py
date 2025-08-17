# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right = ListNode(),ListNode()
        l,r = left ,right
        while head:
            if head.val < x:
                l.next = head 
                l = l.next
            else:
                r.next = head 
                r = r.next 
            head = head.next
        r.next = None  
        l.next = right.next
        return left.next            



