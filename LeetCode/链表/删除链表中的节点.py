"""
 @Description      https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/41/
 @author          linux
 @create          2020-05-12 20:12
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    left = node
    r = node.next
    while r is not None:
        left.val = r.val
        if r.next is None:
            break
        left = r
        r = r.next
    left.next = None

def answer(node):
    node.val = node.next.val
    node.next = node.next.next
