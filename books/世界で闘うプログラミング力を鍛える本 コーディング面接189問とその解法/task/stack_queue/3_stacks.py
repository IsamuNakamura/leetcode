# 複数のスタックを持つクラスの実装
from stack import Stack


class SetOfStacks:
    def __init__(self, size: int):
        self.stacks = []
        self.capacity = size

    def getLastStack(self) -> Stack:
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[len(self.stacks)-1]

    def push(self, data: int):
        lastStack = self.getLastStack()
        if lastStack == None or lastStack.isFull():
            newStack = Stack(self.capacity)
            newStack.push(data)
            self.stacks.append(newStack)
        else:
            lastStack.push(data)

    def pop(self) -> int:
        lastStack = self.getLastStack()
        if lastStack == None:
            print('Stack Underflow!! Calling exit()…')
            exit(-1)
        elif lastStack.isEmpty():
            self.stacks.pop(-1)
            self.pop()
        else:
            return lastStack.pop()

    def __str__(self) -> str:
        s = ''
        for stack in self.stacks:
            s += str(stack) + '\n'
        return s


if __name__ == "__main__":
    stacks = SetOfStacks(2)
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.pop()
    stacks.pop()
    stacks.pop()
    print(stacks)
