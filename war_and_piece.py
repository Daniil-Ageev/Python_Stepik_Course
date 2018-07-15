s = input().lower().split()
[print(i, s.count(i)) for i in set(s)]
