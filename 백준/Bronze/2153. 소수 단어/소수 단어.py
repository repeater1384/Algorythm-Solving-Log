import string

idx_note = ' ' + string.ascii_lowercase + string.ascii_uppercase

word = input()
idx_sum = 0
for c in word:
    idx_sum += idx_note.index(c)

for i in range(2, idx_sum):
    if idx_sum % i == 0:
        print('It is not a prime word.')
        break
else:
    print('It is a prime word.')
