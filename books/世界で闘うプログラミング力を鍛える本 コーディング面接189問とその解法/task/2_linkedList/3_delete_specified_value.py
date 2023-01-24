# 連結リストから指定されたk番目の値を削除

from linked_list import LinkedList

def delete_specified_value(l: LinkedList, index: int) -> LinkedList:
  node = l.get_node(index)
  if node == None:
    return

  node.data = node.next.data
  node.next = node.next.next

  return l




if __name__ == "__main__":
  l = LinkedList()
  data = [1, 2, 3, 4]

  for v in data:
    l.insert_first(v)

  print(delete_specified_value(l, 2))
  print(l)
  # print(delete_specified_value(l, 3))
