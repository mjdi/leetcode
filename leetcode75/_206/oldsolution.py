# https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

from leetcode75.dshelper import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head # []
        if head.next == None:
            return head # [1]
        # [1,2] minimum, therfore swap first two nodes
        curr = None
        if head.next.next : # [1,2,3...]
            curr = head.next.next
        rev = head.next
        rev.next = head
        rev.next.next = None # ensure we point the last node to None

        if not curr:
            return rev # [2,1,None]
         
        # traverse left to right node by node, redirecting the current
        # node to the reversed list of previous nodes up to this point,
        while curr is not None:
            next = curr.next # save next node 
            curr.next = rev # tack on reversed nodes to curr
            rev = curr # update reversed nodes as curr
            curr = next # increment curr
            
        return rev

 