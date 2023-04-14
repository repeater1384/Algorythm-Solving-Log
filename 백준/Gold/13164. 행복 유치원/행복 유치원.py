N, K = map(int, input().split())
arr = [*map(int, input().split())]
diff = [arr[i] - arr[i - 1] for i in range(1, N)]
diff.sort(reverse=True)
print(sum(diff[K - 1:]))
