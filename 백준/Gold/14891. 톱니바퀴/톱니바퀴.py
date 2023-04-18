A,B=[input()for _ in[0]*4],[0]*4
z=lambda n,l:(n+8+l)%8
def C(k,c,p):
    n=k+p
    if n!=-1and n!=4and A[k][z(B[k],2*p)]!=A[n][z(B[n],-2*p)]:C(n,-c,p)
    B[k]=z(B[k],-c)
for _ in[0]*int(input()):
    a,b=map(int,input().split())
    a-=1
    C(a,b,1)
    B[a]=z(B[a],b)
    C(a,b,-1)
print(sum([2**i*(int(A[i][B[i]]))for i in range(4)]))