# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = dummy = ListNode(0, head)
        right = head
        prev = None
        while n > 0:
            right = right.next
            n -= 1
        while right:
            prev = right
            right = right.next
            dummy = dummy.next
        dummy.next = dummy.next.next
        return left.next
