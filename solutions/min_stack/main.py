class MinStack:
    def __init__(self):
        self.stack = collections.deque()
        self.min = collections.deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
