def ccw(_x1, _y1, _x2, _y2, _x3, _y3):
    return (_x2 - _x1) * (_y3 - _y1) - (_y2 - _y1) * (_x3 - _x1)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

# 123, 124, 341, 342
ccw1 = ccw(x1, y1, x2, y2, x3, y3)
ccw2 = ccw(x1, y1, x2, y2, x4, y4)
ccw3 = ccw(x3, y3, x4, y4, x1, y1)
ccw4 = ccw(x3, y3, x4, y4, x2, y2)

answer = 0
if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
        answer = 1
else:
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        answer = 1

print(answer)
