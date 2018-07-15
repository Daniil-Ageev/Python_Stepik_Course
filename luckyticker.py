ticket = int(input())
if ( int(ticket%10) + int(ticket%100//10) + int(ticket%1000//100) == int(ticket//1000%10) + int(ticket//10000%10) + int(ticket//100000)):
    print("Счастливый")
else:
    print("Обычный")