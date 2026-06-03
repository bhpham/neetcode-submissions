# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    #TC: O(k * log(n)) where k is number of linkedlist and n is total nodes across all lists
    #SC: O(k) where heap size is at most k
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        minHeap = []

        for i, node in enumerate(lists):
            heapq.heappush(minHeap, (node.val, i, node))    # (nodeVal, idx, node)
        
        dummy = ListNode()
        cur = dummy
        while minHeap:
            nodeVal, idx, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, idx, node.next))
        
        return dummy.next
