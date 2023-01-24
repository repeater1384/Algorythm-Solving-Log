def merge_sort(orig_list):
    if len(orig_list) == 1:
        return orig_list

    mid = (len(orig_list) + 1) // 2
    sorted_left = merge_sort(orig_list[:mid])
    sorted_right = merge_sort(orig_list[mid:])
    len_left = len(sorted_left)
    len_right = len(sorted_right)

    l, r = 0, 0
    sorted_list = []
    while l < len_left and r < len_right:
        if sorted_left[l] < sorted_right[r]:
            save.append(sorted_left[l])
            sorted_list.append(sorted_left[l])
            l += 1
        else:
            save.append(sorted_right[r])
            sorted_list.append(sorted_right[r])
            r += 1
    while l < len_left:
        save.append(sorted_left[l])
        sorted_list.append(sorted_left[l])
        l += 1
    while r < len_right:
        save.append(sorted_right[r])
        sorted_list.append(sorted_right[r])
        r += 1
    return sorted_list


N, K = map(int, input().split())
arr = [*map(int, input().split())]
save = [-1]
merge_sort(arr)

if K < len(save):
    print(save[K])
else:
    print(-1)
