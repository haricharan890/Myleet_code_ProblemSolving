class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k: return head
        
        last, L = head, 1
        while last.next:
            last = last.next
            L += 1
            
        last.next = head
        for _ in range(L - k % L):
            last = last.next
            
        dummy = last.next
        last.next = None
        
        return dummy