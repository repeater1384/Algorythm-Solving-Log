def solution(babbling):
    answer = 0
    can = ['aya','ye','woo','ma']
    for babb in babbling:
        used = []
        for _ in range(4):
            for c in can:
                if babb[:len(c)] == c and c not in used:
                    used.append(c)
                    babb = babb[len(c):]
        if not babb:
            answer += 1
    return answer