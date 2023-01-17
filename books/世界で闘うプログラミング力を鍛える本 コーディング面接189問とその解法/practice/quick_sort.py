def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]

    # ピボットよりも小さい要素を全て含んだぶんぶん配列
    less = [i for i in arr[1:] if i <= pivot]

    # greater = [i for i in arr[1:] if i > pivot]
    greater = filter(lambda val: val > pivot, arr)
    return quicksort(less) + [pivot] + quicksort(list(greater))

print(quicksort([3, 4, 1, 2]))
