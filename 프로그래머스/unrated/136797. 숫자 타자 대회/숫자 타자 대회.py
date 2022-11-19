def solution(numbers):
    answer = 0
    pos_arr = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    
    wei = {(4,6):0,(6,4):0}
    for num in map(int,numbers):
        next_wei = {}
        for k,v in wei.items():
            a,b = k
            if a == num or b == num:
                if (a,b) in next_wei:
                    next_wei[(a,b)] = min(next_wei[(a,b)],v+1)
                else:
                    next_wei[(a,b)] = v+1
            else:
                dis_from_a = calc_dis(*pos_arr[num],*pos_arr[a]) + v
                dis_from_b = calc_dis(*pos_arr[num],*pos_arr[b]) + v
                if (a,num) in next_wei:
                    next_wei[(a,num)] = min(next_wei[(a,num)], dis_from_b)
                else:
                    next_wei[(a,num)] = dis_from_b
                    
                if (num,b) in next_wei:
                    next_wei[(num,b)] = min(next_wei[(num,b)],dis_from_a)
                else:
                    next_wei[(num,b)] = dis_from_a
        wei = next_wei

    return min(wei.values())



def calc_dis(y,x,i,j):
    if y == i and x == j:
        return 1
    y_diff = abs(y-i)
    x_diff = abs(x-j)
    if y_diff == x_diff:
        return y_diff * 3
    return min(y_diff,x_diff) * 3 + abs(y_diff-x_diff) * 2
