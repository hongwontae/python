# import csv

# with open('weather_data.csv', mode='r') as csv_data :
#     d = csv_data.readlines()
#     print(d)

# with open('./weather_data.csv', mode='r') as csv_data :
#     data = csv.reader(csv_data)
#     tempature = []
#     for partData in data :
#         if partData[1] == 'temp' :
#             pass
#         else :
#             tempature.append(int(partData[1]))
#     print(tempature)

import pandas;

data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])
# print(type(data))
# print(data.to_dict()["day"])
# print(data['temp'].to_list())
# temp_data_list = data['temp'].to_list()
# print(temp_data_list)
# templeng = len(temp_data_list)
# intValue = 0
# for tempOne in temp_data_list :
#     intValue+= tempOne
# print(round(intValue/templeng))

# series에서 max 값을 찾는 방법
# print(data['temp'].max())

# series => object
# 일치하는 값 찾기
print(data[data.day == 'Monday'])

# 일치하는 값 찾기2
# print(data[data.temp == data['temp'].max()])

dictionary_2 = {
    "student" : ['any', 'some', 'every'],
    "scores" : [1, 2, 3]
}

# 딕셔너리 타입 데이터 프레임으로 변환
data_frame_test = pandas.DataFrame(dictionary_2)
print(data_frame_test)

# 데이터 프레임 csv로 변환
data_frame_test.to_csv('new_test.csv')
