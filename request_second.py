import requests


def recursion(http):
    if requests.get(http).text[0] != 'W' and requests.get(http).text[1] != 'e':
        print('https://stepic.org/media/attachments/course67/3.6.3/' + requests.get(http).text)
        recursion('https://stepic.org/media/attachments/course67/3.6.3/' + requests.get(http).text)

    else:
        print(requests.get(http).text)


recursion('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')