def solution(numbers):
    pos_arr = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    INF = 10**10
    wei = {(4,6):0,(6,4):0}
    for num in map(int,numbers):
        next_wei = {}
        for k,v in wei.items():
            a,b = k
            if a == num or b == num:
                next_wei[(a,b)] = min(next_wei.get((a,b),INF),v+1)
            else:
                next_wei[(a,num)] = min(next_wei.get((a,num),INF),calc_dis(*pos_arr[num],*pos_arr[b]) + v)
                next_wei[(num,b)] = min(next_wei.get((num,b),INF),calc_dis(*pos_arr[num],*pos_arr[a]) + v)
        wei = next_wei

    return min(wei.values())



def calc_dis(y,x,i,j):
    y_diff = abs(y-i)
    x_diff = abs(x-j)
    if y_diff == x_diff:
        return y_diff * 3
    return min(y_diff,x_diff) * 3 + abs(y_diff-x_diff) * 2
