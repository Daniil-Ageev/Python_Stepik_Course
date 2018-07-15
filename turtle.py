ox = [["север", 0], ["восток", 0], ["запад", 0], ["юг", 0]]
x = [str(input()).split(' ') for _ in range(int(input()))]
for i in range(len(x)):
    if x[i][0] == "север":
        ox[0][1] = ox[0][1] + int(x[i][1])
    if x[i][0] == "юг":
        ox[3][1] = ox[3][1] + int(x[i][1])
    if x[i][0] == "восток":
        ox[1][1] = ox[1][1] + int(x[i][1])
    if x[i][0] == "запад":
        ox[2][1] = ox[2][1] + int(x[i][1])
print(str(ox[1][1] - ox[2][1]) + " " + str(ox[0][1] - ox[3][1]))
