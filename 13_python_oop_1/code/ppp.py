from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Player', ['Nunez', 'Salah', 'Diaz'])
table.add_column('Goals', ['2', '5', '3'])
print(table)