"""
给定头，即链表的头，确定链表中是否有循环。
如果链表中有某个节点可以通过连续跟随下一个指针来再次访问节点本身，就有一个循环。
在内部，pos用于表示尾部的下一个指针所连接的节点的索引。
请注意，pos不作为参数传递。

如果链表中有一个循环，则返回true。
否则，返回false。

您可以使用O（1）（即常量）内存来解决它吗？
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 双指针版
def solution(head):
    if not head:
        return False
    slow = head
    fast = head.next
    # 由于环的存在，fast必定可以追上slow
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


# 数组保存已遍历的
def solution2(head):
    if head:
        stack = [head]
        head = head.next
        while head:
            if head not in stack:
                stack.append(head)
                head = head.next
            else:
                return True
    return False


n3 = ListNode(3, next=None)
n2 = ListNode(2, next=n3)
n1 = ListNode(1, next=n2)
n3.next = n3
# print(solution(n1))
print(solution2(n1))