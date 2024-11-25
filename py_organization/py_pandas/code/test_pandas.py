import pandas;

states_data_frame = pandas.read_csv('50_states.csv')
# 요약 정보
# print(states_data_frame.info())
# # 상위 5개 정보 반환
# print(states_data_frame.head())
# # 하위 5개 정보 반환
# print(states_data_frame.tail())

# (행수, 열수) 튜플 타입으로 반환
# print(states_data_frame.shape)
# # 칼럼 이름
# print(states_data_frame.columns)
# # 데이터 통계 요약
# print(states_data_frame.describe())


# 특정 열 확인 => Series
# print(states_data_frame['x'])
# 여러 열 확인x => DataFrame
# print(states_data_frame[['x', 'state']])
