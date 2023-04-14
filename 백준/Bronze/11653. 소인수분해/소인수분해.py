def solution(n):
    if n != 1:
        while n:
            for i in range(2,int(n**0.5)+1):
                if n%i ==0:
                    print(i)
                    n//=i
                    break
            else:
                print(n)
                break
# for i in range(1,10000001):
#     try:
#         solution(i)
#     except:
#         print(i)
#         break
solution(n = int(input()))