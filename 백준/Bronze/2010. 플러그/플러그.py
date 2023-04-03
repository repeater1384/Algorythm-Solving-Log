import sys
size = int(sys.stdin.readline())
answer = [0] * size
for i in range(size):
    answer[i] += int(sys.stdin.readline())
print(sum(answer)-size+1)