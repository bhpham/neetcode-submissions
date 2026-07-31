# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Questions:
1/ what is the length of l1? 1 <= 100 
2/ what is the length of l2? 1 <= 100
3/ Are we only considering single digit number? yes [0 - 9]

input: l1 = [1,2,3], l2 = [4,5,6]
output: [5,7,9]

321 + 654 = 975

My straight forward approach is:
1/ iterate each list node
2/ convert the node -> value
3/ add them up
4/ check value of number by checking if > 9. e.g: 13 % 10 = 3
5/ carry: e.g: 13 / 10 = 1
6/ add a new tail node, pointing to value we got 

TC: O(max(M, N)) where M is the number of nodes in l1 and N is the number of nodes in l2
SC: O(max(M, N)) 
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        dummy = curr 
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        

             







