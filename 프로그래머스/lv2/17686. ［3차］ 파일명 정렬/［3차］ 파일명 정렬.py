def solution(files):
    answer = []
    for file in files:
        head,number = split_file(file)
        answer.append((head, number,file))
    answer.sort(key = lambda x:(x[0],x[1]))
    return [a[2] for a in answer]

def split_file(file):
    file = file + '!'
    for i in range(len(file)):
        if '0' <= file[i] <= '9':
            for j in range(i,len(file)):
                if not ('0' <= file[j] <= '9'):
                    return file[:i].upper(),int(file[i:j])