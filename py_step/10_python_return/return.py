def function_1() :
    """hello-world"""
    return 'HWT'

def function_2() :
    return 111

def function_3(text) :
    return text.title()

data_1 = f'{function_3(function_1())}-{function_2()}'
print(data_1)