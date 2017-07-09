# noinspection PyInterpreter
def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        val = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > val:
                lists[j + 1] = lists[j]
                lists[j] = val
            j -= 1
    return lists

print(insert_sort([6, 4, 9, 6, 3, 2, 0]))


def str_reverse(string):
    if isinstance(string, str):
        ls = list(string)
        l = len(ls)
        for i, j in zip(range(l-1, 0, -1), range(l//2)):
            ls[i], ls[j] = ls[j], ls[i]
        return ''.join(ls)
    else:
        return 'must be string'

print(str_reverse(''))
