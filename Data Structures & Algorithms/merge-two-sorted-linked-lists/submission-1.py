# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        curr1 = list1
        curr2 = list2

        head = None

        if curr1.val < curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next
        sortcurr = head

        while curr1 and curr2:
            if curr1.val < curr2.val:
                sortcurr.next = curr1
                curr1 = curr1.next
            else:
                sortcurr.next = curr2
                curr2 = curr2.next
            sortcurr = sortcurr.next

        while curr1:
            sortcurr.next = curr1
            curr1 = curr1.next
            sortcurr = sortcurr.next
        while curr2:
            sortcurr.next = curr2
            curr2 = curr2.next
            sortcurr = sortcurr.next

        return head
                

        