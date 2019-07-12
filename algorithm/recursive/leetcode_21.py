# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        vir_node = ListNode(0)
        cur_node = vir_node
        while l1 is not None or l2 is not None:
            if l1 is None:
                cur_node.next = ListNode(l2.val)
                cur_node = cur_node.next
                l2 = l2.next
            elif l2 is None:
                cur_node.next = ListNode(l1.val)
                cur_node = cur_node.next
                l1 = l1.next
            elif l1.val < l2.val:
                cur_node.next = ListNode(l1.val)
                cur_node = cur_node.next
                l1 = l1.next
            else:
                cur_node.next = ListNode(l2.val)
                cur_node = cur_node.next
                l2 = l2.next
        return vir_node.next
