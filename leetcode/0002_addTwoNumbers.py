class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head, cur = None, None
        while l1 or l2:
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next

            value += carry
            if head:
                cur.next = ListNode(value % 10)
                cur = cur.next
            else:
                head = cur = ListNode(value % 10)

            carry = value // 10

        if carry:
            cur.next = ListNode(carry)
        return head


# 测试部分
t1 = ListNode(9)
t2 = ListNode(4)
t3 = ListNode(9)
t1.next = t2
t2.next = t3

e1 = ListNode(5)
e2 = ListNode(6)
e3 = ListNode(4)
e1.next = e2
e2.next = e3

s = Solution()
res = s.addTwoNumbers(t1, e1)
while res:
    print(res.val)
    res = res.next
