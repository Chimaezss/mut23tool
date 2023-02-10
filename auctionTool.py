# Instructions for tool usage
print('1) Snipe Tool')
print('2) "Lazy Buy" Tool')
print('3) Set Tool')
print('Enter 1, 2, or 3')

chosenMode = input()
enteredPrice = 0
if chosenMode == '1':
    print('Enter price of card(-1 to quit): ')
    enteredPrice = input()
    while enteredPrice != '-1':
        print('Enter desired profit: ')
        desiredProfit = input()
        buyPrice = (int(enteredPrice) * .90) - int(desiredProfit)
        print(f'You should buy at {buyPrice} for a profit of {desiredProfit}.')
        print('Enter price of card(-1 to quit): ')
        enteredPrice = input()
elif chosenMode == '2':
    print('What is the overall range? ')
    overallRange = input()
    print(f'What is the "Lazy" price for {overallRange}\'s?')
    enteredPrice = input()
    buyPrice = int(enteredPrice) * .60
    print(f'You should buy {overallRange}\'s for {buyPrice}.')
elif chosenMode == '3':
    allCardPrices = []
    totalSetCost = 0
    while enteredPrice != '-1':
        print('Enter price of set card: ')
        enteredPrice = input()
        if enteredPrice != '-1':
            allCardPrices.append(int(enteredPrice))
    for i in allCardPrices:
        totalSetCost += i
    print('What is the card going for?')
    buyPrice = input()
    afterTaxPrice = int(buyPrice) * .9
    profit = afterTaxPrice - totalSetCost
    print(f'The set has a net of {profit} coins.')
