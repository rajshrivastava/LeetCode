# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap = []
        resultHead = ListNode()
        for i in range(len(lists)):
            if lists[i]:
                heappush(minHeap, (lists[i].val, i))
                lists[i] = lists[i].next

        ptr = resultHead
        while minHeap:
            val, idx = heappop(minHeap)
            ptr.next = ListNode(val)
            ptr = ptr.next
            if lists[idx]:
                heappush(minHeap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return resultHead.next
