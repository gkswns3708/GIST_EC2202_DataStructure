def bin_search(start: int, end: int, lst: list, target_value: int):
    if start > end:
        return 0
    else:
        mid = (start + end) // 2
        mid_value = lst[mid]
        if mid_value == target_value:
            return 1
        elif mid_value > target_value:
            return bin_search(start, mid - 1, lst, target_value)
        elif mid_value < target_value:
            return bin_search(mid + 1, end, lst, target_value)


N = int(input())
num_lst = list(map(int, input().split()))
M = int(input())
target_num_lst = list(map(int, input().split()))

num_lst.sort()

for num in target_num_lst:
    print(bin_search(0, N - 1, num_lst, num))
