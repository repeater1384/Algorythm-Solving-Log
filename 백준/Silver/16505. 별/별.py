n=int(input())
a = [[' ' for _ in range(pow(2,n))] for _ in range(pow(2,n))]

def printStar(x,y,size):
    if size == 0:
        a[x][y] = '*'
        return
    else:
        printStar(x,y,size-1)
        printStar(x,y+pow(2,size-1),size-1)
        printStar(x+pow(2,size-1),y,size-1)

printStar(0,0,n)

for x in a:
    print(''.join(x).rstrip())
