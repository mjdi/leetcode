# https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

from leetcode75.dshelper.linked_list import ListNode
from typing import Optional

# https://leetcode.com/problems/reverse-linked-list/solutions/6550282/0ms-100-step-by-step-visualization-easiest-to-understand-java-c-python/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev

 