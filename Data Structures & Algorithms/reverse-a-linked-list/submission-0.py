# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        prev = None

        while curr is not None:

            # store next node
            next = curr.next

            # reverse curr node next pointer
            curr.next = prev

            # move pointers one position ahead
            prev = curr
            curr = next

        return prev
