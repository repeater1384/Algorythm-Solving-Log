word = input()


def change(_word):
    word_type = None

    for w in _word:
        if w.isupper():
            word_type = 'java'

    if '_' in _word:
        word_type = 'error' if word_type else 'c++'

    if len(_word.split('_')) == 1:
        if _word.split('_')[0].islower():
            word_type = 'c++'

    if '__' in _word or _word[-1] == '_' or word[0].isupper() or word[0] == '_':
        word_type = 'error'

    if word_type == 'c++':
        temp = _word.split('_')
        changed_word = ''
        for i in range(len(temp)):
            if i != 0:
                changed_word += temp[i].capitalize()
            else:
                changed_word += temp[i]
        return changed_word

    elif word_type == 'java':
        changed_word = ''
        for w in _word:
            if w.isupper():
                changed_word += '_' + w.lower()
            else:
                changed_word += w
        return changed_word
    else:
        return 'Error!'


print(change(word))
