def solution(string):
    
    conv_sub = []
    for temp in string.split(' '):
        conv_temp = ''
        for idx, s in enumerate(temp):
            if idx % 2 == 0:
                conv_temp += s.upper()
            else:
                conv_temp += s.lower()
        conv_sub.append(conv_temp)
    return ' '.join(conv_sub)