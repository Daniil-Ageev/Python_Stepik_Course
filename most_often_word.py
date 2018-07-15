array_str = list()
with open("file.txt", "r") as inf:
    for line in inf:
        lines = line.lower()
        string = str()
        i = 0
        while i < len(lines):
            j = i
            while not lines[j].isspace():
                string = string + lines[j]
                j = j + 1
                i = j
                if j == len(lines):
                    break
            i = i + 1
            array_str.append(string)
            string = str()

most_often_word = str()
how_often = 0
temp_often = 0
for i in range(len(array_str)):
    j = i
    while j < len(array_str):
        if array_str[j] == array_str[i]:
            temp_often = temp_often + 1
        j = j + 1
    if temp_often > how_often:
        most_often_word = array_str[i]
        how_often = temp_often
    elif temp_often == how_often and array_str[i] < most_often_word:
        most_often_word = array_str[i]
        how_often = temp_often
    temp_often = 0
print(most_often_word + " " + str(how_often))