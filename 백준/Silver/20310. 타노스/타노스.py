S = input()


# print('0' * (S.count('0') // 2) + '1' * (S.count('1') // 2))

def delete_char(word, char, cnt):
    del_cnt = 0
    word = [*word]
    idx = 0
    while del_cnt < cnt:
        if word[idx] == char:
            word[idx] = ''
            del_cnt += 1

        idx += 1

    return ''.join(word)


S = delete_char(S, '1', S.count('1') // 2)
print(delete_char(S[::-1], '0', S.count('0') // 2)[::-1])
