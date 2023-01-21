def urlify(s: str, length:int) -> str:
  spaceCount = s[:length].count(' ')
  idx = length + spaceCount * 2 # 空白を"%20"に変換するので2倍(空白分は既に与えられた長さに含まれる)

  # 新規にメモリを確保しないため、文字列の後ろから探していき変換していく
  for i in range(length-1, -1, -1):
    if s[i] == ' ':
      print("if")
      print(i)

      print(s[:idx-3])
      print(s[idx:])
      # pythonだと文字列に直接代入できないので、分割して結合
      s = s[:idx-3] + '%20' + s[idx:]
      print(s)

      idx -= 3
    else:
      print("else")
      print(i)

      print(s[:idx-1])
      print(s[idx:])

      s = s[:idx-1] + s[i] + s[idx:]
      print(s)

      idx -= 1

  return s

print(urlify("Mr John Smith      ",13))
# print(urlify("I S  A  M U        ",11))
# print(urlify("I S A M U        ",9))
# print(urlify("I S  A M U        ",10))

# def urlify(s: str, length:int) -> str:
#   convertStr = []
#   count = 0

#   for c in s:
#     count += 1
#     if c == ' ':
#       convertStr.append("%20")
#     else:
#       convertStr.append(c)
#     if count == length: break
#   return ''.join(convertStr)
