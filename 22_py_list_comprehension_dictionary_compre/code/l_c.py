# new_list = [1,2,3]

# data = [n*2 for n in new_list]
# print(data)

# new_str = 'Hong Won Tae'.replace(' ', '')

# data_2 = [n for n in new_str]
# print(data_2)

# new_range = range(8)
# data_3 = [n*2 for n in new_range]
# print(data_3)

# new_names = ['Hong', 'An ji yeon', 'zlatan', 'marcous', 'Eric-simmins']
# data_4 = [n.upper() for n in new_names if len(n) >= 8]
# print(data_4)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
print(numbers)
