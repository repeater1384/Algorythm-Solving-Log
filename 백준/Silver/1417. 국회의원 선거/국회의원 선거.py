N = int(input())
arr = [int(input()) for _ in range(N)]
my_val = arr.pop(0)
answer = 0

while arr:
    max_val = max(arr)
    if my_val > max_val:
        break
    idx = arr.index(max_val)
    my_val += 1
    arr[idx] -= 1
    answer += 1
    
print(answer)
