# リストの中の要素数を抽出

def count(arr):
  if arr == []:
    return 0
  else:
    return 1 + count(arr[1:])

print(count([1,2,3]))
print(count([1,2,3,4,5]))
print(count([]))
