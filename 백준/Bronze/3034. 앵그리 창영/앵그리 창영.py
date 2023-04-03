N, W, H = map(int, input().split())
dialog = (W * W + H * H) ** .5
for _ in range(N):
    print('DA' if dialog >= int(input()) else 'NE')