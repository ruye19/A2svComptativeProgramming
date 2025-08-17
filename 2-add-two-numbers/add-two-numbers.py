# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        curr = output 
        reminder,last = 0,0
        while l1 or l2 or reminder:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            sumval = value1 + value2 + reminder 
            reminder= sumval // 10
            last = sumval % 10
            curr.next = ListNode(last)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return output.next    
