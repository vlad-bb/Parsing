# def sort_list(unsort_list: list):
#     unsort_list.sort()
#     return unsort_list
#
#
# firrst = [1, 2, 4, 10, 12, 0, 5]
# first_list = sort_list(firrst)
# second = ['one', 'two', 'aba', 'zore', 'task']
# secon_list = sort_list(second)
#
# print(first_list, secon_list)

# num = int(input("Enter an integer number: "))
#
# # is_even = True if num%2 == 0 else False
# is_even = (True, False)[num%2]
# print(is_even)
import pickle

filename = '/Users/admin/Documents/GitHub/Parsing/babypark/draft/goods_urls_set.bin'
with open(filename, 'rb') as file:
    urls = pickle.load(file)
    print(len(urls))
