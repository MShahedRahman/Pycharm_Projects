
def selection_sort(lst):
    for i in range(0, len(lst)):
        minpos = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minpos]:
                minpos = j

        temp = lst[i]
        lst[i] = lst[minpos]
        lst[minpos] = temp

        print(lst)


lst = [5,3,8,6,7,2]
selection_sort(lst)
print(lst)

