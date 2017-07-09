def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i+1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

print(select_sort([3, 7, 5, 1, 8, 0]))
