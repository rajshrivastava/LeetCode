# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # n1, n2 = len(l1), len(l2)
        # n = min(n1, n2)
        carry = 0
        #total = 0
        l3 = ListNode(0)
        ptr = l3
        # for _ in range(n):
        while l1 and l2:
            ptr.next = ListNode(0)
            ptr = ptr.next
            
            add = l1.val + l2.val
            ptr.val =  (add + carry)%10
            carry = (add + carry)//10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            ptr.next = ListNode(0)
            ptr = ptr.next
            
            ptr.val = (l1.val + carry)%10
            carry = (l1.val + carry)//10
            l1 = l1.next
        
        while l2:
            ptr.next = ListNode(0)
            ptr = ptr.next
            
            ptr.val = (l2.val + carry)%10
            carry = (l2.val + carry)//10
            l2 = l2.next
        
        if carry:
            ptr.next = ListNode(carry)
            
        return l3.next
