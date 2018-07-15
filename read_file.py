ouf = open("output.txt", "w")
with open("file.txt", "r") as inf:
    line = inf.readline()
    s = str()
    digit = 0
    for i in range(len(line)):
        if not line[i].isdigit():
            s = s + line[i]
        else:
            if line[i+1].isdigit():
                for k in range(int(line[i])*10 + int(line[i+1])):
                    ouf.write(s)
            else:
                for j in range(int(line[i])):
                    ouf.write(s)
                del s
            s = str()
ouf.close()