# 素数チェック

import math

def isPrime(num):
  if num < 1:
    return None
  print(math.isqrt(num))
  for i in range(2, math.isqrt(num), 1):
    if num % i == 0:
      return 'not prime'
  return 'prime'


print(isPrime(33))
print(isPrime(2))
print(isPrime(0))
