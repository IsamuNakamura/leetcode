# a³+b³=c³+d³を満たす全ての整数解を出力。ただし、a,b,c,dは1から1000までとする。

import math
def three_dim_equation():
  n = 10
  for a in range(1, n, 1):
    for b in range(1, n, 1):
      for c in range(1, n, 1):
        d = math.pow(math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3), 1//3)
        d = int(d)
        if math.pow(a, 3) + math.pow(b, 3) == math.pow(c, 3) + math.pow(d, 3) and 0 <= d and d <=n:
          print(a, b, c, d)

  # n = 10
  # resultMap = {}
  # for c in range(1, n, 1):
  #   for d in range(1, n, 1):
  #     result = math.pow(c, 3) + math.pow(d, 3)
  #     resultMap[result] = [c, d]
  # for a in range(1, n, 1):
  #   for b in range(1, n, 1):
  #     result = math.pow(a, 3) + math.pow(b, 3)
  #     if result in resultMap:
  #       print(a,b, resultMap[result])
  # for v1 in resultMap.values():
  #   for v2 in resultMap.values():
  #     print(v1,v2)

print(three_dim_equation())
