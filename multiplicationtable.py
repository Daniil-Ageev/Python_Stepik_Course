import sys
a = int(input())
b = int(input())
c = int(input())
d = int(input())
sys.stdout.write("\t")
for i in range(c, d + 1):
    sys.stdout.write(str(i) + "\t")
print()
for j in range(a, b+1):
    sys.stdout.write(str(j) + "\t")
    for i in range(c, d+1):
        sys.stdout.write(str(i*j) + "\t")
    print()
