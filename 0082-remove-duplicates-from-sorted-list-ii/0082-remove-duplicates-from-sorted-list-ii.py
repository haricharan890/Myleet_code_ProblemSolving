# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = dummyTail = curr = ListNode(-150)
        dummyTail.next = head
        while curr:
            if (curr.next and curr.val == curr.next.val) or (curr.next and curr.next.next and curr.next.val == curr.next.next.val):
                curr = curr.next
                continue
            dummyTail.next = curr.next
            dummyTail, curr = dummyTail.next, curr.next
        return dummyHead.next

        