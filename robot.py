a = int(input())
b = a % 10
c = a % 100
if (c >= 11) and (c <= 19):
    print(str(a) + " программистов")
elif b == 1:
    print(str(a) + " программист")
elif (b >= 2) and (b <= 4):
    print(str(a) + " программиста")
elif b >= 5:
    print(str(a) + " программистов")
elif b == 0:
    print(str(a) + " программистов")
