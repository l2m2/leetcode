'''
@File: main.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-12 22:08:02
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-12 22:12:55
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        cur = fake_head
        while l1 or l2:
            if not l1:
                cur.next = l2
                break
            if not l2:
                cur.next = l1
                break

            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        return fake_head.next


if __name__ == "__main__":
    so = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3

    m1 = ListNode(1)
    m2 = ListNode(3)
    m3 = ListNode(4)
    m1.next = m2
    m2.next = m3

    result = so.mergeTwoLists(n1, m1)

    while result:
        print(result.val)
        result = result.next