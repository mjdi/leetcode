from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def write_linked_list(head: ListNode) -> str:
    li = ''
    current = head
    while current:
        li = li + str(current.val) + " -> "
        current = current.next
    return li + "None"
    
def create_linked_list(vals: List) -> ListNode:
    if len(vals) == 0:
        return None
    head = ListNode(vals[0])
    start = head
    for val in vals[1:]:
        head.next = ListNode(val)
        head = head.next
    return start

def compare_linked_lists(head1: ListNode, head2: ListNode) -> bool:
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return head1 is None and head2 is None

