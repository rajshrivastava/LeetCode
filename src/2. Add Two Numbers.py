# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = l1
        while l1 and l2:
            carry, add = divmod(l1.val + l2.val + carry, 10)
            l1.val = add
            ptr = l1
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            carry, add = divmod(l1.val + carry,10)
            l1.val = add
            ptr=l1
            l1 = l1.next
        
        while l2:
            carry, add = divmod(l2.val + carry,10)
            ptr.next = ListNode(add)
            ptr = ptr.next
            l2 = l2.next
        
        if carry:
            ptr.next = ListNode(carry)
        return head
