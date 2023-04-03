for _ in range(int(input())):
    store_length = int(input())
    start_x, start_y = map(int, input().split())
    stores = [[*map(int, input().split())] for _ in range(store_length)]
    ex, ey = map(int, input().split())
    stores.append((ex, ey))

    stack = [(start_x, start_y)]
    visited = [(start_x, start_y)]
    result = 'sad'
    while stack:
        cx, cy = stack.pop()
        # print(cx, cy)
        if cx == ex and cy == ey:
            result = 'happy'
            break

        for store in stores:
            sx, sy = store
            if (sx, sy) not in visited:
                if abs(sx - cx) + abs(sy - cy) <= 1000:
                    stack.append((sx, sy))
                    visited.append((sx, sy))

    print(result)
