"""
给定一个二叉树，返回其节点值的preorder先序遍历。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
"""
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
后续：递归解决方案很简单，您可以迭代吗？
"""


def traversal(root, lst):
    if root:
        lst.append(root.val)
        traversal(root.left, lst)
        traversal(root.right, lst)
class Solution:
    def preorderTraversal(self, root: TreeNode):
        lst = []
        traversal(root, lst)

        return lst


n3 = TreeNode(3, None, None)
n2 = TreeNode(2, n3, None)
n1 = TreeNode(1, None, n2)
lst = []
traversal(n1, lst)
print(lst)


