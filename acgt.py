a = input()
i = 0
j = len(a)
k = 0
s = 9
string = ""
while i < j:
    string = string + a[i]
    k = i
    s = 0
    while a[i] == a[k]:
        k = k + 1
        s = s + 1
        if(k > len(a) - 1):
            break
    string = string + str(s)
    i = k
print(string)