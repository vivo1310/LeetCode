class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # storing min val only

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = val
        if self.minStack:
            minVal = min(val, self.minStack[-1])
        self.minStack.append(minVal)
        # minVal = min(val, self.minStack[-1] if self.minStack else val)
        # self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()