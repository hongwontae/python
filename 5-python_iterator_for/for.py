# works = ['Aaaaple', "Banana", "Peach"]

# for w in works :
#     print(w)
#     print(w + 'pie')


s_point = [100,200,300,400,500,999,444, 2000, 3999, 9090,2]
data = 0
choice_data = []


def loopfunction() :
    global data
    for single in s_point :
        if single > data :
            data = single
            choice_data.append(single)

loopfunction()

print(choice_data[len(choice_data)-1])

        

