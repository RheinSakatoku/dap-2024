list1 = list(map(int, input(" Список 1, вводи цифры через пробел ").split()))
list2 = list(map(int, input(" Список 2, вводи цифры через пробел ").split()))

def concater(list1, list2):
    concated_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            concated_list.append(list1[i])
            i += 1
        else:
            concated_list.append(list2[j])
            j += 1

    while i < len(list1):
        concated_list.append(list1[i])
        i += 1

    while j < len(list2):
        concated_list.append(list2[j])
        j += 1
    return concated_list

print(concater(list1, list2))