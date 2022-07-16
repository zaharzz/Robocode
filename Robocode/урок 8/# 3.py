fill = 0
base = 0
def triangle(fill, base):
    for i in range(0, base+1):
        print(fill * i)
    for s in range(base-1, 0, -1):
        print(s*fill)
fill = str(input())
base = int(input())
triangle(fill, base)
