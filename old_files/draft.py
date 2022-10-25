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
# import pickle
#
# filename = '/Users/admin/Documents/GitHub/Parsing/babypark/draft/goods_urls_set.bin'
# with open(filename, 'rb') as file:
#     urls = pickle.load(file)
#     print(urls)
# some = [1]
# if len(some) == 0:
#     print('emtpy')
# elif len(some) > 0:
#     print('not none')

# result = None
# operand = None
# operator = None
# wait_for_number = True
#
# while True:
#     user_input = input(">>> ")
#     if user_input == '=':
#         break
#
#     if wait_for_number:
#         try:
#             operand = float(user_input)
#         except ValueError:
#             print("Not a Number")
#             continue
#
#         wait_for_number = False
#
#         if not result:
#             result = operand
#         if operator == "=":
#             print(result)
#             break
#
#         else:
#             if operator == '+':
#                 result += operand
#             if operator == '-':
#                 result -= operand
#             if operator == '*':
#                 result *= operand
#             if operator == '/':
#                 try:
#                     result /= operand
#                 except ZeroDivisionError:
#                     print("Ділення на 0")
#                     continue
#     else:
#         if user_input in ('+', '-', '*', '/'):
#             operator = user_input
#         else:
#             operator = None
#
#         if not operator:
#             print("Not operator")
#         else:
#             wait_for_number = True


