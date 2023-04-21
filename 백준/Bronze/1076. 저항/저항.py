color = ['black', 'brown', 'red',
         'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
a, b, c = [color.index(input()) for _ in range(3)]
answer = int(str(a) + str(b)) * (10 ** c)
print(answer)
