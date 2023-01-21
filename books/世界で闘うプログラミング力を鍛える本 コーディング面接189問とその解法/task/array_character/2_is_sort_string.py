from collections import defaultdict

def is_sort_string(s1:str, s2:str) -> bool:
  if len(s1) != len(s2): return False
  if len(s1) > 128 or len(s2) > 128: return False

  stringMap = defaultdict(int)
  for c in s1: stringMap[c] += 1

  for c in s2:
    if c in stringMap:
      stringMap[c] -= 1
      if stringMap[c] < 0:
        return False
    else:
      return False
  return True


print(is_sort_string("dog", "god"))
print(is_sort_string("Dog", "god"))
print(is_sort_string("dog", "god "))
print(is_sort_string("sdfasdfa","asdfasdf"))
