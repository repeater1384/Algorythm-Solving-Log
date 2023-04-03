import sys

input = sys.stdin.readline

div_num = int(1e9 + 7)
answer = 0

for _ in range(int(input())):
    C, K = map(int, input().split())
    answer = (answer + C * K * pow(2, K - 1, div_num)) % div_num

print(answer % div_num)
