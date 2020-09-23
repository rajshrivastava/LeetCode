# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        n = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            n += 1
        ptr.next = head
        
        newTail = head
        for i in range(n - k%n -1):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        
        return newHead
