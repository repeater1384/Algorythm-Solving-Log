table = {}
temp = ['ACAG', 'CGTA', 'ATCG', 'GAGT']
A = 'AGCT'
for i in range(4):
    for j in range(4):
        table[A[i] + A[j]] = temp[i][j]
input()
data = [*input()]
while len(data) > 1:
    a, b = data.pop(), data.pop()
    data.append(table[a + b])
print(data[0])
