N = int(input())
can_make = False
temp = N // 5

while temp >= 0:
    left = N - temp * 5
    if left % 3 == 0:
        print(temp + left // 3)
        can_make = True
        break
    else:
        temp -= 1

if can_make is False:
    print(-1)