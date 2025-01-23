data = {
    0 : 'HWT',
    1 : 'GGG'
}

new_dict = {key*2 : value for (key, value) in data.items()}
print(new_dict)