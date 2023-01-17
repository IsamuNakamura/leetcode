def binary_search(arr, item):
  low = 0
  high = len(arr)-1

  while low <= high:
    mid = (low + high) // 2
    guess = arr[mid]
    print("mid: %f" % mid)
    print("guess: %f \n" % guess)

    if guess == item:
       return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binary_search(l, 3))

print(binary_search(l, 1))
