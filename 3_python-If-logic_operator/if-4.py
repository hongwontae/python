p_size = input('choice your service S, M, L')
p_number = int(input('choice your number'))
bill = 0

if p_size == 'S' :
    print(f'Size S and price {bill}')
    bill+=10
elif p_size == 'M' : 
    bill+=20
    print(f'Size M and price {bill}')
elif p_size == 'L' :
    bill+=30
    print(f"Size L and price {bill}")
else :
    print('Correct data Please!')
