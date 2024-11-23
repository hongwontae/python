bids = {}
should_continue = True

def bid_function(bid) :
    winner = ''
    hightest_price = 0

    for name in bid :
        if bid[name] > hightest_price :
            hightest_price = bid[name]
            winner = name
    print(f'winner is {winner} price is {hightest_price}')

while should_continue :
    name = input('What is Your name? \n')
    price = int(input('What is your bid? \n'))
    bids[name] = price
    go_away = input('bid keep going? yes or no \n')
    if go_away == 'no' :
        should_continue = False
        bid_function(bids)
    else :
        should_continue = True
        
