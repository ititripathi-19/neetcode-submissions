class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        pass

    def pop(self) -> None:
        self.stack.pop()
        pass

    def top(self) -> int:
        n= len(self.stack)
        return self.stack[n-1]

    def getMin(self) -> int:
        minS = min(self.stack)
        return minS
