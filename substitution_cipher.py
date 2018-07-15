alph = [i for i in input()]
cipher = [i for i in input()]
to_cipher = [i for i in input()]
to_uncipher = [i for i in input()]
new_cipher = list()
new_uncipher = list()
for i in range(len(to_cipher)):
    for j in range(len(cipher)):
        if alph[j] == to_cipher[i]:
            new_cipher.append(cipher[j])
            break
for i in range(len(to_uncipher)):
    for j in range(len(alph)):
        if cipher[j] == to_uncipher[i]:
            new_uncipher.append(alph[j])
            break
for i in range(len(new_cipher)):
    print(new_cipher[i], end="")
print()
for i in range(len(new_uncipher)):
    print(new_uncipher[i], end="")
#print()