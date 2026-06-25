# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        prev = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev


        while head and second:
            first = head.next
            nxt = second.next
            head.next = second
            second.next = first
            head = first
            second = nxt
        
