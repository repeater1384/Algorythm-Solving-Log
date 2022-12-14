w, h, f, c, x1, y1, x2, y2 = map(int, input().split())

area = (x2 - x1) * (y2 - y1) * (c + 1)
answer = w * h - area
if f * 2 <= w:
    if f > x1:
        answer -= (min(f, x2) - x1) * (y2 - y1) * (c + 1)
else:
    if x1 + f < w:
        answer -= (min(w, f + x2) - (f + x1)) * (y2 - y1) * (c + 1)
print(answer)
