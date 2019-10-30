#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        # else:
        #     raise LookupError('stack is empty!')

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        # else:
        #     raise LookupError('stack is empty!')

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = Stack()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minStack.stack:
            if x <= self.minStack.top():
                self.minStack.push(x)
        else:
            self.minStack.push(x)

    def pop(self) -> None:
        if self.stack: 
            if self.top() == self.minStack.top():
                self.minStack.pop()
            self.stack.pop()
        # else:
        #     raise LookupError('stack is empty!')

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        # else:
        #     raise LookupError('stack is empty!')

    def getMin(self) -> int:
        return self.minStack.top()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# x = 1
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end