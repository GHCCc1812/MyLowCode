import math


def prime_list(end, start=1):
    i = int(start)
    end = int(end) + 1
    if not (i % 2):
        i += 1  # 使成为奇数
    list_p = []
    if i < 2:
        list_p += [2]
        i = 3
    while i < end:
        j = int(math.sqrt(i))
        m = 3
        while m <= j:
            if (i % m) == 0:
                break
            else:
                m += 2
        else:
            list_p += [i]
        i += 2
    return list_p
