'''
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input: 5

Sample Output:

1 2 3 4 5       (0 0) (0 1) (0 2) (0 3) (0 4)
16 17 18 19 6   (1 0) (1 1) (1 2) (1 3) (1 4)
15 24 25 20 7   (2 0) (2 1) (2 2) (2 3) (2 4)
14 23 22 21 8   (3 0) (3 1) (3 2) (3 3) (3 4)
13 12 11 10 9   (4 0) (4 1) (4 2) (4 3) (4 4)

Sample Input: 3

Sample Output:

1 2 3
8 9 4
7 6 5

'''
a = int(input())
i = 0
j = 0
while i < a:
    while j < a:
        print(j, end=" ")
        j = j + 1
    i = i + 1