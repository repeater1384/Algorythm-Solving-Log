for _ in range(int(input())):
    list = [input().split()[-1] for _ in range(int(input()))]
    freq = {}
    for item in list:
        if freq.get(item) == None:
            freq[item] = 2
        else:freq[item]+=1
    try:
        print(eval('*'.join([str(value)for value in freq.values()]))-1)
    except SyntaxError:
        print(0)