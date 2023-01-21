# 連結リストの後ろから指定されたk番目の値を取得

from linked_list import LinkedList

def extract_data_from_tail(l: LinkedList, searchIndex: int) -> int:
  current_node = l.head
  if current_node == None:
    return
  count = 0
  while current_node != None:
    count +=1
    if count == searchIndex:
      return current_node.data
    current_node = current_node.next





if __name__ == "__main__":
  l = LinkedList()
  data = [1, 2, 3, 4]

  for v in data:
    l.insert_first(v)

  print(extract_data_from_tail(l, 1))

  l1 = LinkedList()
  print(extract_data_from_tail(l1, 1))
