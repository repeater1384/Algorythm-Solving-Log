def solution():
    word = input()
    length = len(word)
    candidate = []
    for i in range(1, length - 1):
        for j in range(i + 1, length):
            candidate.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

    candidate.sort()
    return candidate[0]

print(solution())