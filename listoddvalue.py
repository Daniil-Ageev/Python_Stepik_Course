def modify_list(l):
    i = len(l) - 1
    while i >= 0:
        if l[i] % 2 == 1:
            del l[i]
        else:
            l[i] = l[i]//2
        i = i - 1


lst = [1, 3, 5, 7]
modify_list(lst)
print(lst)
