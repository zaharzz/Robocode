import math
otvet = 0
a = float(input())
a1 = math.ceil(a)
otvet += a1
a1 = math.floor(a)
otvet += a1
print(otvet)