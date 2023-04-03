def permutate(arr,r):

    check = [0] * len(arr)
    choose = []

    def generate():
        if len(choose) == r:
            print(*choose)
            return
        else:
            for i in range(len(arr)):
                if check[i] == 0:
                    check[i] = 1
                    choose.append(arr[i])
                    generate()
                    choose.pop()
                    check[i] = 0
    generate()

n,m = map(int,input().split())
arr = [*map(int,input().split())]
permutate(sorted(arr),m)