for l in range(int(input())):
    a=sorted(list(map(int,input().split()))[1:])
    print('Class %d\nMax %d, Min %d, Largest gap %d'%(l+1,max(a),min(a),max([a[i+1]-a[i]for i in range(len(a)-1)])))