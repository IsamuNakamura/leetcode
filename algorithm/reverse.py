# リスト反転

def reverse(arr):
  for i, num in enumerate(arr):
    if i == len(arr)//2:
      return arr
    reverseIndex = len(arr) - i - 1
    temp = num
    arr[i] = arr[reverseIndex]
    arr[reverseIndex] = temp

l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(reverse(l))
