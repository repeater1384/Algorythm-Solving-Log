import sys

input = sys.stdin.readline

N = int(input())
prices = [[*map(int, input().split())] for _ in range(N)]
prices.sort(key=lambda x: x[1])

# temp1[i] : i+1부터 N-1의 원소중 ai의 최솟값
# temp2[i] : 0부터 i까지의 원소중 ai-bi의 최솟값

temp1, temp2 = [0] * N, [0] * N

temp1[N - 1] = prices[N - 1][0]

for i in range(N - 2, -1, -1):
    temp1[i] = min(temp1[i + 1], prices[i][0])

temp2[0] = prices[0][0] - prices[0][1]
for i in range(1, N):
    temp2[i] = min(prices[i][0]-prices[i][1], temp2[i - 1])

prefix_sum = 0
for i in range(N):
    # prefix_sum = 0부터 i까지, bi의 누적합
    prefix_sum += prices[i][1]

    # case1
    # 하나를 ai로 바꿔야 하는데, 바꿀 음식이 i+1~N 사이에 있는 경우
    # 가격의 총합의 변동은 해당 범위에서의 ai의 최솟값을 더하고, 마지막에 더한 bi를 뺌(bi로 정렬했으므로)
    case1 = prefix_sum + temp1[i] - prices[i][1]

    # case2
    # 하나를 ai로 바꿔야 하는데, 바꿀 음식이 0~i 사이에 있는 경우
    # 가격의 총합의 변동은 +ai - bi 이므로, ai-bi의 최솟값을 더함
    case2 = prefix_sum + temp2[i]

    print(min(case1, case2))
