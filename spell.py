x = set(input().lower() for o in range(int(input())))
y = set(' '.join(input().lower() for o in range(int(input()))).split())
print(*(x - y), sep='\n')
