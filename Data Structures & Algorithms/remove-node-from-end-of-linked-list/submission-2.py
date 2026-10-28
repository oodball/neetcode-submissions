# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next

        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next
        
        i = count - n
        curr = head

        if i == 0:
            return head.next

        for j in range(count - 1):
            if (j + 1) == i:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head

        