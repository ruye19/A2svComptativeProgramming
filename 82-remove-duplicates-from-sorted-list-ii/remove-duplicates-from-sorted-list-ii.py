# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # Pointer to keep track of the current node
        current = head
        prev = None  # To track the previous node for connecting unique nodes

        while current:
            # Check if current node is part of a duplicate sequence
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Now 'current' is the last duplicate node, move 'current' to the next unique node
                if prev:
                    prev.next = current.next  # Skip all duplicates
                else:
                    # If no previous node, it means we are at the head, so update head
                    head = current.next
            else:
                # If no duplicates, move 'prev' to current node
                prev = current

            # Move current to the next node
            current = current.next

        return head