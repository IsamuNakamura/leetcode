from binary_tree import Node, BinaryTree
import random

map = {}

def binary_tree_depth_list(root: Node) -> int:
  if root == None:
    return 0

  # print("root: %d" % root.data)
  # print("max: %d" % max(get_depth(root.right), get_depth(root.left)))

  val = 1 + max(binary_tree_depth_list(root.left), binary_tree_depth_list(root.right))
  # print("val: %d" % val)
  if map.get(val) == None:
      map[val] = [root.data]
  else:
      map[val].append(root.data)
  return val

if __name__ == "__main__":
  # l = [random.randint(0, 100) for _ in range(7)]
  l = [1, 2, 3, 4, 5, 6, 7]
  l.sort()
  print(l)
  bt = BinaryTree(l)
  root = bt.create_min_binary_tree()
  # print(bt.get_depth(root))
  binary_tree_depth_list(root)
  print(map)
