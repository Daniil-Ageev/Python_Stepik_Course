a = int(input())
i = 1
s = 0
while True:
    j = 0
    while j < i:
        print(i, end=" ")
        s = s + 1
        j = j + 1
        if s == a:
            exit(0)
    i = i + 1