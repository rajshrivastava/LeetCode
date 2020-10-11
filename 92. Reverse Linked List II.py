# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(node, count):
            prev = None
            curr = node
            for i in range(count):
                next_ = curr.next
                curr.next = prev
                prev= curr
                curr = next_
            
            node.next = curr
            return prev
            
        if not head or not head.next:
            return head
        curr, prev = head, None
        i = 1
        while curr and i<m:
            prev = curr
            curr = curr.next
            i += 1
            
        if prev:
            prev.next = reverse(curr, n-m+1)
        else:
            head = reverse(curr, n-m+1)
        
        return head
        
