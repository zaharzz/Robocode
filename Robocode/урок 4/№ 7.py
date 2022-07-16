from email.quoprimime import body_length


a = input("")
b = input("")
c = input("")
min1 = min(len(a), len(b), len(c))
max1 = max(len(a), len(b), len(c))
if min1 == len(a):
    print(a)
elif min1 == len(b):
    print(b)
elif min1 == len(c):
    print(c)
if max1 == len(a):
    print(a)
elif max1 == len(b):
    print(b)
elif max1 == len(c):
    print(c)
