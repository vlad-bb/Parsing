def sort_list(unsort_list: list):
    unsort_list.sort()
    return unsort_list


firrst = [1, 2, 4, 10, 12, 0, 5]
first_list = sort_list(firrst)
second = ['one', 'two', 'aba', 'zore', 'task']
secon_list = sort_list(second)

print(first_list, secon_list)
