# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        curr, prev = head, None

        # while curr is not None
        while curr:
            # store the next node temporarily
            temp = curr.next 
            # reverse the link so that the curr node points back to the prev node
            curr.next = prev
            # move prev the curr node
            prev = curr
            # make the curr node the temporarily stored node
            curr = temp
        # return the new head
        return prev 
