class Stack:

    # Stackを初期化
    def __init__(self, size):
        self.arr = [None for _ in range(size)]
        self.capacity = size
        self.top = -1

    # 要素の追加
    def push(self, data: int):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)

        self.top = self.top + 1
        self.arr[self.top] = data

    # 最上位の要素を削除して返す
    def pop(self) -> int:
        # アンダーフローのチェック
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)

        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    # 最上位の要素を削除せずに返す
    def peek(self) -> int:
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]

    # スタックのサイズを返す
    def size(self) -> int:
        return self.top + 1

    # スタックが空かどうかをチェック
    def isEmpty(self) -> bool:
        return self.size() == 0

    # スタックがいっぱいかどうかをチェック
    def isFull(self) -> bool:
        return self.size() == self.capacity

    def __str__(self) -> str:
        if self.isEmpty():
            return "This Stack is null"
        s = ""
        for i in range(self.size()):
            s += "{}->".format(self.arr[i])
        return s


if __name__ == '__main__':

    stack = Stack(3)

    stack.push(1)
    stack.push(2)

    # stack.pop()
    # stack.pop()

    stack.push(3)
    # stack.push(1)

    # print('Top element is', stack.peek())
    # print('The stack size is', stack.size())

    # stack.pop()

    # if stack.isEmpty():
    #     print('The stack is empty')
    # else:
    #     print('The stack is not empty')

    print(stack)
