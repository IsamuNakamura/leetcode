# 深さが最小になる二分探索木の作成
from binary_tree import BinaryTree
import random

if __name__ == "__main__":
  l = [random.randint(0, 100) for _ in range(11)]
  l.sort()
  print(l)
  bt = BinaryTree(l)
  root = bt.create_min_binary_tree(0, len(l)-1)
  print(root.data)
  print(root.left.data)
  print(root.right.data)
  print(root.left.left.data)
  print(root.left.right.data)
  print(root.right.left.data)
  print(root.right.right.data)
