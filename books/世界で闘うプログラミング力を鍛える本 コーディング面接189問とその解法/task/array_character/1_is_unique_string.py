def is_unique_string(s: str) -> bool:
  if len(s) > 128:
    return False

  uniqueStr = {}
  for c in s:
    if c in uniqueStr:
      return False
    uniqueStr[c] = True

  return True


print(is_unique_string("abcde"))
print(is_unique_string("abbde"))
print(is_unique_string("abcbe"))
