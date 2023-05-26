class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_pos(self):
        return (*self.point1.get_pos(), *self.point2.get_pos())


def ccw(_x1, _y1, _x2, _y2, _x3, _y3):
    return (_x2 - _x1) * (_y3 - _y1) - (_y2 - _y1) * (_x3 - _x1)


def is_intersect(line1, line2):
    x1, y1, x2, y2 = line1.get_pos()
    x3, y3, x4, y4 = line2.get_pos()

    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

    # 123, 124, 341, 342
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)

    # 두 선분에 일직선 상에 있을때
    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True
    else:
        # 일반적인 상황
        if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
            return True
    return False


def find(x):
    global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    global parents
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


N = int(input())
parents = [i for i in range(N)]
lines = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append(Line(Point(x1, y1), Point(x2, y2)))

for i in range(N - 1):
    for j in range(i + 1, N):
        if is_intersect(lines[i], lines[j]):
            union(i, j)

freq = {}
for parent in map(find, parents):
    freq[parent] = freq.get(parent, 0) + 1

print(len(freq.keys()))
print(max(freq.values()))
