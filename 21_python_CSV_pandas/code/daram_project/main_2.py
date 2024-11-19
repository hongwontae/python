import pandas;

data = pandas.read_csv('./daram.csv')
data_list = data['Primary Fur Color'].to_list()
grey_daram = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_datam = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_daram = len(data[data['Primary Fur Color'] == 'Black'])

print([grey_daram, cinnamon_datam, black_daram])

# for data_2 in data_list :
#     if data_2 == 'Gray' :
#         pass
#     else :
#         print(data_2)

dic_daram_color = {
    "daram_color" : ['Gray', 'Cinnamon', 'Black'],
    "count" : [grey_daram, cinnamon_datam, black_daram]
}

data_frame_daram_count = pandas.DataFrame(dic_daram_color)
data_frame_daram_count.to_csv('daram_count.csv', index=False)