"""
反转单链列表。
可以迭代或递归地反向链接列表。
你能同时实现吗？
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head):
    backup = head
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    lst.reverse()
    # print(lst)
    head = backup
    i = 0
    while head:
        head.val = lst[i]
        i += 1
        head = head.next
    return backup


def solution2(head):
    hh = ListNode(0)
    hh.next = head
    if head:
        w = head.next
        h = head  # h指向已经反转部分的最后一个节点
        while w:
            k = w.next
            w.next = hh.next  # 放到头部
            h.next = k

            hh.next = w  # 放到第一个
            w = k
    return hh.next


n3 = ListNode(3, next=None)
n2 = ListNode(2, next=n3)
n1 = ListNode(1, next=n2)
# solution(n1)
solution2(n1)
# head = n1
while n1:
    print(n1.val)
    n1 = n1.next
