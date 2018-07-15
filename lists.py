a = [int(i) for i in input().split()]
a.sort()
i = 1
first = a[0]
already = False
if len(a) == 2 and a[0] == a[1]:
    print(a[1])
while i < len(a) - 1:
    j = i
    while j < len(a):
        if a[j] == first and not already:
            print(first, end=" ")
            already = True
        if a[i] != first:
            first = a[j]
            already = False
        j = j + 1
    i = i + 1
