# スタックの最小の要素を返す

import sys
from stack import Stack

class Stack_min(Stack):
  def __init__(self, size):
    super().__init__(size)
    # 最小の要素を格納するデータ
    self.min_data = Stack(size)

  def push(self, data:int):
    super().push(data)

    # 格納するデータが最小の要素よりも小さい場合に追加
    if self.min() > data:
      self.min_data.push(data)

  def pop(self):
    top = super().pop()

    # 最上位の要素が最小の要素と同じ場合、最小の要素を削除
    if self.min() == top:
      self.min_data.pop()
    return top

  # 最小の要素を返す
  def min(self) -> int:
    if self.min_data.isEmpty():
      return sys.maxsize
    else:
      return self.min_data.peek()

  def __str__(self):
    return self.min_data.__str__()

if __name__ == '__main__':
  stack = Stack_min(3)

  stack.push(2)
  stack.push(1)
  stack.push(3)
  print(stack.min())
  print(stack.min())
