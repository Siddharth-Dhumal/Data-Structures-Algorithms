class MinStack:

    def __init__(self):
        self.minStack = []
        self.minTrack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if not self.minTrack or self.minTrack[-1] >= val:
            self.minTrack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.minTrack[-1]:
            del self.minTrack[-1]
        del self.minStack[-1]

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minTrack[-1]