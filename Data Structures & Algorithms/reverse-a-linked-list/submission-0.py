# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if head is None or head.next is None:
            return head

        # 2 node example

        # head: node1
        # val = 100
        # next = node2

        # node2
        # val = 30
        # next = None

        curr = head
        prev = None
        temp = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
