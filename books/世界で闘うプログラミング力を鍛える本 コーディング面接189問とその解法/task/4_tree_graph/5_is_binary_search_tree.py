# 二分木が二分探索木か
from binary_tree import BinaryTree, Node
import random

def check_binary_search_tree(root:Node) -> bool:
  return is_binary_search_tree(root, None, None)

def is_binary_search_tree(n:Node, min:int, max:int) -> bool:
  if n == None:
    return True

  if (min != None and n.data <= min ) or (max != None and n.data > max):
    return False

  if (is_binary_search_tree(n.left, min, n.data) == False) or (is_binary_search_tree(n.right, n.data, max) == False):
    return False

  return True



if __name__ == "__main__":
  l = [random.randint(0, 100) for _ in range(7)]
  l.sort()
  bt = BinaryTree(l)
  root = bt.create_min_binary_tree(0, len(l)-1)
  print(check_binary_search_tree(root))
