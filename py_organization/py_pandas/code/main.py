import pandas as pd

with open('./50_states.csv') as file :
    file_csv = pd.read_csv(file)
    print(file_csv)