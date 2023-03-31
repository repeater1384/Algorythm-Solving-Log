N = int(input())
K = int(input())
arr = [*map(int, input().split())]
arr.sort()
diff = [arr[i + 1] - arr[i] for i in range(N - 1)]
diff.sort(reverse=True)
print(sum(diff[K - 1:]))
