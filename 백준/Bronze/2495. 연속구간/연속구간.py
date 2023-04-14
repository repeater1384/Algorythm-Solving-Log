for _ in range(3):
    a = input()

    answer = 1

    for i in range(7):
        temp = 0
        for j in range(i, 8):
            if a[i] == a[j]:
                temp += 1
            else:
                break
        answer = max(answer, temp)

    print(answer)
