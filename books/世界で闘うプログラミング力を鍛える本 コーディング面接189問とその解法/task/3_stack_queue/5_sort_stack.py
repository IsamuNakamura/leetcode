from stack import Stack


def sort(s: Stack) -> Stack:
    subStack = Stack(5)
    while s.isEmpty() == False:
        top = s.pop()

        # ソートするスタックのトップよりも補助スタックのトップが大きかったらソートするスタックに追加
        while subStack.isEmpty() == False and subStack.peek() > top:
            s.push(subStack.pop())
        subStack.push(top)
    print(subStack.arr)
    while subStack.isEmpty() == False:
        s.push(subStack.pop())
    print(s.arr)
    return s.arr


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    sort(stack)


# [3, 5, 2, 4] 1 []
# [3, 5, 2, 4] [1]

# [3, 5, 2] 4 [1]
# [3, 5, 2][1, 4]

# [3, 5] 2 [1, 4]
# [3, 5, 4] 2 [1]
# [3, 5, 4] [1, 2]

# [3, 5] 4 [1, 2]
# [3, 5][1, 2, 4]

# [3] 5 [1, 2, 4]
# [3][1, 2, 4, 5]

# [] 3 [1, 2, 4, 5]
#     [5] 3 [1, 2, 4]
#     [5, 4] 3 [1, 2]
# [5, 4] [1, 2, 3]

# [5] 4 [1, 2, 3]
# [5] [1, 2, 3, 4]

# [] 5 [1, 2, 3, 4]
# [] 5 [1, 2, 3, 4, 5]
