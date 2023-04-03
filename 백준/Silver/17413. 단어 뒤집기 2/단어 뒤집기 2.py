word = input() + ' '

temp = ''
idx = 0

while idx < len(word):
    if word[idx] == ' ':
        print(temp[::-1], end=' ')
        temp = ''
    elif word[idx] == '<':
        print(temp[::-1], end='')
        temp = ''

        next_tag = word.find('>', idx)
        print(f'{word[idx:next_tag + 1]}', end='')
        idx = next_tag
    else:
        temp += word[idx]

    idx += 1