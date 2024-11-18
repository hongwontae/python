PLACEHOLDER = "[name]"

with open('./input/Names/invited_names.txt') as file :
    data2 = file.readlines()
    print(data2)

with open('./input/Letters/starting_letter.txt') as file :
    file_data = file.read()
    for name in data2 :
        stripped_name = name.strip()
        new_letter = file_data.replace(PLACEHOLDER, stripped_name)
        print(new_letter)