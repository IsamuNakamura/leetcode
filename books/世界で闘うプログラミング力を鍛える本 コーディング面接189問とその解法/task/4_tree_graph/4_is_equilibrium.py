# 二分木が平衡かどうか(全てのノードが持つ2つの部分木の高さの差が1つ以下であるような木)
from binary_tree import BinaryTree, Node
import random

def get_depth(root:Node) -> int:
  if root == None:
    return 0

  return 1 + max(get_depth(root.left), get_depth(root.right))

def is_equilibrium(root: Node) -> bool:
  if root == None:
    return True

  if abs(get_depth(root.left) - get_depth(root.right)) > 1:
    return False
  else:
    return is_equilibrium(root.left) and is_equilibrium(root.right)


if __name__ == "__main__":
  l = [random.randint(0, 100) for _ in range(7)]
  l.sort()
  bt = BinaryTree(l)
  root = bt.create_min_binary_tree(0, len(l)-1)
  print(is_equilibrium(root))
