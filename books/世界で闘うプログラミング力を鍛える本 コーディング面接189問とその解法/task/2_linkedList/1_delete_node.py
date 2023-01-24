# 連結リストから重複をなくす

from linked_list import LinkedList

def deleteNode(l: LinkedList) -> LinkedList:
  nodeMap = {}
  current_node = l.head
  previous_node = LinkedList()

  while current_node is not None:
    if current_node.data in nodeMap:
      previous_node.next = current_node.next
    else:
      nodeMap[current_node.data] = True
      previous_node = current_node
    current_node = current_node.next
  return l

# # 別のメモリを使用しない方法
# def deleteNode(l: LinkedList) -> LinkedList:
#   current_node = l.head
#   while current_node is not None:
#     runner = current_node
#     while runner.next is not None:
#       if runner.next.data == current_node.data:
#         runner.next = runner.next.next
#       else:
#         runner = runner.next
#     current_node = current_node.next
#   return l

if __name__ == "__main__":
  l = LinkedList()
  data = [1,2,3,4,2,1,3,5,2,2,4]

  for v in data:
    l.insert_first(v)

  print(deleteNode(l))
