# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75
from leetcode75.dshelper.linked_list import ListNode
from typing import Optional
                
class Solution:
    @staticmethod
    def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next:
            slow, fast = head, head.next

            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next

            slow.next = slow.next.next  # remove middle
        else:
            head = None
        return head

