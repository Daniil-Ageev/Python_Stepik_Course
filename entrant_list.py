with open("file.txt", encoding="utf8") as inf:
    average_math = 0
    average_physic = 0
    average_russia = 0
    entrant_count = 0
    for line in inf:
        entrant_count = entrant_count + 1
        average = list(line.split(';'))
        average_math = average_math + float(average[1])
        average_physic = average_physic + float(average[2])
        average_russia = average_russia + float(average[3])
        print((float(average[1]) + float(average[2]) + float(average[3]))/3)
print(str(average_math/entrant_count) + " " + str(average_physic/entrant_count) + " " + str(average_russia/entrant_count))