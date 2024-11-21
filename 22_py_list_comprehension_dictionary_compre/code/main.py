import pandas;

students_socrs = {
    'student' : ['Alexander', 'Kiesa', 'Robertson', 'Graven-berch'],
    'score' : [75, 30, 70, 90]
}

data_frame_student = pandas.DataFrame(students_socrs)
print(data_frame_student)
data_list = []

# series
# print(data_frame_student.score)
# # 일치하는 series 행을 찾습니다.
# print(data_frame_student[data_frame_student.score == 30])
for (index, row) in data_frame_student.iterrows() :
    print(row.score)

# for (key, value) in data_frame_student.items() :
#     data_list.append(key)

# print(data_list)
# print('???')

# for (index, row) in data_frame_student.iterrows() :
#     print(row)
#     data_list.append(row.student)
# print(data_list)

# print(data_frame_student.student[0])12

