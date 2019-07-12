# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        vir_node = ListNode(0)
        cur = head
        while cur is not None:
            next_node = cur.next
            cur.next = vir_node.next
            vir_node.next = cur
            cur = next_node
        return vir_node.next
