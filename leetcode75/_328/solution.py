# https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
from leetcode75.dshelper.linked_list import ListNode
                
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(Q_head: Optional[ListNode]) -> Optional[ListNode]:
        if Q_head is None or Q_head.next is None:
            return Q_head

        Q_next = Q_head.next
        odd_node, even_node = Q_head, Q_head.next
        node = even_node
        odd_even = 0  # 0 for odd, 1 for even

        while (node := node.next) is not None:
            if odd_even == 0:
                odd_node.next = node
                odd_node = odd_node.next
            else:
                even_node.next = node
                even_node = even_node.next
            odd_even = 0 if odd_even == 1 else 1
        if odd_even == 1:
            # remove odd node from even_node
            even_node.next = None

        odd_node.next = Q_next
        return Q_head
