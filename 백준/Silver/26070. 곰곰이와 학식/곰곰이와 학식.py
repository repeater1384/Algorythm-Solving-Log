ABC = [*map(int, input().split())]
XYZ = [*map(int, input().split())]

answer = 0
for i in range(3):
    if ABC[i] > XYZ[i]:
        answer += XYZ[i]
        ABC[i] -= XYZ[i]
        XYZ[i] = 0
    else:
        answer += ABC[i]
        XYZ[i] -= ABC[i]
        ABC[i] = 0

n_XYZ = [0, 0, 0]
for i in range(3):
    n_XYZ[i] = XYZ[(i + 2) % 3] // 3
XYZ = n_XYZ

for i in range(3):
    if ABC[i] > XYZ[i]:
        answer += XYZ[i]
        ABC[i] -= XYZ[i]
        XYZ[i] = 0
    else:
        answer += ABC[i]
        XYZ[i] -= ABC[i]
        ABC[i] = 0

n_XYZ = [0, 0, 0]
for i in range(3):
    n_XYZ[i] = XYZ[(i + 2) % 3] // 3
XYZ = n_XYZ

for i in range(3):
    if ABC[i] > XYZ[i]:
        answer += XYZ[i]
        ABC[i] -= XYZ[i]
        XYZ[i] = 0
    else:
        answer += ABC[i]
        XYZ[i] -= ABC[i]
        ABC[i] = 0
print(answer)