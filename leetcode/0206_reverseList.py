# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur

        # cur, nxt = None, None
        # while head:
        #     nxt = head.next
        #     head.next = cur
        #     cur = head
        #     head = nxt
        return cur
