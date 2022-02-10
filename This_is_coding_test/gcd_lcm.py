# 최대공약수(GCD)

def gcd(a, b):
  while b != 0:
    result = b
    a, b = b, a % b
    return result
  

# 최소공배수(LCM)

def lcm(a, b):
  return int(a * b / gcd(a, b))
