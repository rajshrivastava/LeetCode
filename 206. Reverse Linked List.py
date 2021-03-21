# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        if not head:
            return head
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr.next = prev
        return curr
        
