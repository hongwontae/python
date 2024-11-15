# number_data = 10

# while number_data < 100 :
#     number_data+=10
#     print(number_data)


my_f_data = 0

def my_function(data) :
    global my_f_data
    my_f_data+=data
    return my_f_data

while my_function(10) < 100 :
    print(my_f_data)
