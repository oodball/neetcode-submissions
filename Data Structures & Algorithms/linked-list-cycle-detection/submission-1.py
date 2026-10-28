# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head.next:
            return False
        curr = head
        fast = curr.next.next

        while fast:
            if fast == curr:
                return True
            fast = fast.next.next
            curr = curr.next
        return False

