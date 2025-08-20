from leetcode75.dshelper import ListNode
from typing import Optional

# https://leetcode.com/problems/reverse-linked-list/solutions/6628448/master-recursive-reversal-unlock-the-cleanest-way-to-reverse-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = Solution.reverseList(head.next)
        head.next.next = head
        head.next = None 
        return new_head
