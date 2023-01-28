class Node:
  def __init__(self, data):
    self.data = data
    self.right:Node = None
    self.left:Node = None

class BinaryTree:
  def __init__(self, l:list):
    self.list = l

  def create_min_binary_tree(self, start:int, end:int) -> Node:
      if start > end:
        return

      mid = (start + end) // 2

      n = Node(self.list[mid])
      n.left = self.create_min_binary_tree(start, mid-1)
      n.right = self.create_min_binary_tree(mid+1, end)

      return n

  def print_node(self, n:Node):
    if n != None:
      self.print_node(n.left)
      self.print_node(n.data)
      self.print_node(n.right)

  def print_tree(self, n:Node):
    self.print_node(n.root)
