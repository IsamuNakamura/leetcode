# 2つのスタックでキューを実装

from stack import Stack


class MyQueue:
    def __init__(self, size: int):
        self.stackNewest = Stack(size)  # 新しい要素を追加していく
        self.stackOldest = Stack(size)  # 古い要素を格納(空になったら、新しい要素群を追加)

    def append(self, data: int):
        self.stackNewest.push(data)

    # 古い要素が無くなったら、新しい要素群を新しい順に古い要素に追加していく
    def stackShift(self):
        if self.stackOldest.isEmpty():
            while self.stackNewest.isEmpty() == False:
                self.stackOldest.push(self.stackNewest.pop())

    def popLeft(self) -> int:
        self.stackShift()
        return self.stackOldest.pop()

    def peek(self) -> int:
        self.stackShift()
        return self.stackOldest.peek()

    def __str__(self) -> str:
        s = ""
        for v in self.stackOldest.arr:
            s += str(v)
        for v in self.stackNewest.arr:
            s += str(v)
        return s


if __name__ == "__main__":
    queue = MyQueue(5)

    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print(queue.peek())
    print(queue.popLeft())
    print(queue.peek())
    print(queue.popLeft())
    print(queue.peek())
    print(queue.popLeft())
    print(queue.peek())
    print(queue.popLeft())
    print(queue.peek())
    print(queue)
