a = int(input(""))
b = int(input(""))
c = int(input(""))
if a == b == c:
    print("Рівносторонній")
elif a == c and a > b:
    print("Рівнобедренний")
elif b == c and b > a:
    print("Різносторонній")