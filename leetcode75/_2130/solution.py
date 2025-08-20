# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75 
from leetcode75.dshelper.linked_list import ListNode
from typing import Optional

class Solution:
    @staticmethod
    def pairsum(head: Optional[ListNode]) -> int:
        # use slow/fast runners to get to middle/end
        # reversing everything to the left of the slow
        prev_slow = None
        slow, fast = head, head.next 
        while fast and fast.next:
            new_slow = slow.next
            # reverse list as we pass by
            slow.next = prev_slow
            prev_slow = slow
            # advance runners
            slow = new_slow
            fast = fast.next.next
        # once at the middle, simultaenously traverse 
        # left and right sides and add up pairs to find max sum
        right = slow.next
        slow.next = prev_slow
        left = slow
        maxsum = left.val + right.val
        while left is not None and right is not None:
            maxsum = max(maxsum, left.val + right.val)
            left, right = left.next, right.next
        return maxsum

