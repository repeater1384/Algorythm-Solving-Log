sum_score, cnt = 0, 0
score_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
while True:
    try:
        _, num, score = input().split()
    except EOFError:
        break
    if score == 'P':
        continue
    sum_score += score_dict[score] * float(num)
    cnt += float(num)
print(sum_score / cnt)
