"""
设计一个堆栈，该堆栈支持在常数时间内push，pop，top和检索最小元素。

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

方法pop，top和getMin将始终在非空堆栈上被调用。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = list()

    def push(self, x: int) -> None:
        self.store.append(x)

    def pop(self) -> None:
        self.store.pop()

    def top(self) -> int:
        return self.store[-1]

    def getMin(self) -> int:
        return min(self.store)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 快了10倍的方法：
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack= []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        # 放入元素时就比较了大小！节省了很多时间
        if not self.stack:self.stack.append((x,x))
        else:
           self.stack.append((x,min(x,self.stack[-1][1])))

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack: self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][0]
        else: return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][1]
        else: return None