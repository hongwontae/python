import pandas;

states_data_frame = pandas.read_csv('./50_states.csv')
dict_states = states_data_frame.to_dict('records')
print(dict_states)