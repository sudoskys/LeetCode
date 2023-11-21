# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        l1.val += l2.val  # 将两数相加，赋值给 l1 节点
        if l1.val >= 10:
            # 如果 l1.val >= 10，说明需要进位，将进位的值赋值给 l1.next
            l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)
            l1.val %= 10  # l1.val 取余 10，保证 l1.val < 10，保证递归的正确性
            # 这里的 l1.next 传入的是一个新的节点，值为 l1.val // 10，这样就可以保证 l1.next.val < 10
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1


def test_solution():
    s = Solution()
    pre = ListNode(0)
    pre.next = ListNode(2)
    pre.next.next = ListNode(4)
    pre.next.next.next = ListNode(3)
    after = ListNode(0)
    after.next = ListNode(5)
    after.next.next = ListNode(6)
    after.next.next.next = ListNode(4)
    res = s.addTwoNumbers(pre.next, after.next)
    assert res.val == 7
