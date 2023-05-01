word = input()

joi_count, ioi_count = 0, 0
for idx in range(len(word) - 2):
    if word[idx] == 'J':
        if word[idx + 1] == 'O' and word[idx + 2] == 'I':
            joi_count += 1
    elif word[idx] == 'I':
        if word[idx + 1] == 'O' and word[idx + 2] == 'I':
            ioi_count += 1

print(joi_count)
print(ioi_count)
