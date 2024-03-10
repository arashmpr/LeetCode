# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        root = head
        heads = {}
        while head:
            i += 1
            heads[i] = head
            head = head.next
        if i-n == 0:
            return root.next
        heads[i-n].next = heads[i-n].next.next
        return root