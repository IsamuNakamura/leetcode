# リストの中の最大値を抽出

def max(arr):
  # biggest = 0
  # if arr == []:
  #   return None
  # else:
  #   for n in arr:
  #     if n > biggest:
  #       biggest = n
  #     else:
  #       continue
  # return biggest
  if arr == []:
    return None

  if len(arr) == 2:
    return arr[0] if arr[0] > arr[1] else arr[1]
  sub_max = max(arr[1:])
  return arr[0] if arr[0] > sub_max else sub_max

print(max([1,2,3]))
print(max([1,2,3,4,5]))
print(max([]))
