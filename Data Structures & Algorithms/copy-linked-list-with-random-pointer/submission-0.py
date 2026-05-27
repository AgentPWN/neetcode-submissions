"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dupe = {None : None}
        cur = head
        while cur:
            dupe[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = dupe[cur]
            copy.next = dupe[cur.next]
            copy.random = dupe[cur.random]
            cur = cur.next
        return dupe[head]