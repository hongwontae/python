try :
    age = int(input('How old are you?'))
except  :
    print(f'you have in a an invalid number. Please try again with a numerical \n')
    age = int(input('How old you? \n'))

if age > 18 :
    print('you can drive at age')