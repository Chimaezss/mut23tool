from pathlib import Path

def initializeTool(prices, overall_range):
    print('Let\'s add a new overall range.')
    sell_price = input('What price can you find those at? ')
    buy_price = float(sell_price) * .8
    print(f'Let\'s start buying at {buy_price}.')
    prices[f'{overall_range}'] = {
        'Sell Price': sell_price,
        'Buy Price': buy_price
    }
    return prices

def salesReport():
    sell_attempts = input('How many cards did you try to sell? ')
    successful_sales = input('How many cards succesfully sold? ')
    sell_percentage = (int(successful_sales) / int(sell_attempts)) * 100
    return sell_percentage

def priceAdjust(sell_percentage, overall_range, prices):
    if sell_percentage <= 30:
        print('That wasn\'t a good hour... lets lower the prices')
        prices[f'{overall_range}']['Sell Price'] = float(prices[f'{overall_range}']['Sell Price']) * .98
        prices[f'{overall_range}']['Buy Price'] = float(prices[f'{overall_range}']['Sell Price']) * .8
    elif sell_percentage <= 50:
        print('We could do better, let\'s lower by a bit.')
        prices[f'{overall_range}']['Sell Price'] = float(prices[f'{overall_range}']['Sell Price']) * .99
        prices[f'{overall_range}']['Buy Price'] = float(prices[f'{overall_range}']['Sell Price']) * .8
    elif sell_percentage <= 70:
        print('That was optimal, lets try maintaining this result.')
    elif sell_percentage <= 100:
        print('That was too good... let\'s try to raise the prices a bit.')
        prices[f'{overall_range}']['Sell Price'] = float(prices[f'{overall_range}']['Sell Price']) * 1.02
        prices[f'{overall_range}']['Buy Price'] = float(prices[f'{overall_range}']['Sell Price']) * .8
    return prices

if Path('./Config Settings.txt').is_file(): # Setup config settings file or use the existing one
    file = open('Config Settings.txt')
    config_settings = []
    for line in file:
        config_settings.append(line[:-1])
    print(config_settings)
else:
    config_settings = ['Initialized: 0']

while True:
    if config_settings[0][-1:] == '0': # First time use procedure
        prices = {}
        print('Welcome to the Madden AH Tool. Let\'s begin with some basics.')
        overall_range = input('What overall\'s are you viewing? ')
        prices = initializeTool(prices, overall_range)
        sell_percentage = salesReport()
        prices = priceAdjust(sell_percentage, overall_range, prices)
        print('Relist cards at: ' + str(prices[f'{overall_range}']['Sell Price']))
        print('Buy new cards at: ' + str(prices[f'{overall_range}']['Buy Price']))
        config_settings.append(f'{overall_range}')
        config_settings.append(prices[f'{overall_range}']['Sell Price'])
        config_settings.append(prices[f'{overall_range}']['Buy Price'])
        config_settings[0] = 'Initialized: 1'
    else: # Using tool after first time
        prices = {}
        print('Welcome back to the Madden AH Tool.')
        overall_range = input('What overall\'s are you viewing? ')
        prices[f'{overall_range}'] = {}

        for x in range(len(config_settings)): # Setup overall range and see if that range has established prices already
            if config_settings[x] == overall_range:
                priceIndex = x + 1
                prices[f'{overall_range}']['Sell Price'] = config_settings[priceIndex]
                prices[f'{overall_range}']['Buy Price'] = config_settings[priceIndex+1]
                overall_found = True
                break
            else:
                overall_found = False
        
        if not overall_found: # Setup a new overall range
            prices = initializeTool(prices, overall_range)
            sell_percentage = salesReport()
            prices = priceAdjust(sell_percentage, overall_range, prices)
            print('Relist cards at: ' + str(prices[f'{overall_range}']['Sell Price']))
            print('Buy new cards at: ' + str(prices[f'{overall_range}']['Buy Price']))
            config_settings.append(f'{overall_range}')
            config_settings.append(prices[f'{overall_range}']['Sell Price'])
            config_settings.append(prices[f'{overall_range}']['Buy Price'])

        else: # Use an existing overall range
            print('Relist cards at: ' + str(prices[f'{overall_range}']['Sell Price']))
            print('Buy new cards at: ' + str(prices[f'{overall_range}']['Buy Price']))
            sell_percentage = salesReport()
            prices = priceAdjust(sell_percentage, overall_range, prices)
            config_settings[priceIndex] = prices[f'{overall_range}']['Sell Price']
            config_settings[priceIndex+1] = prices[f'{overall_range}']['Buy Price']
            print('Relist cards at: ' + str(prices[f'{overall_range}']['Sell Price']))
            print('Buy new cards at: ' + str(prices[f'{overall_range}']['Buy Price']))

    file = open('Config Settings.txt', 'w') # Put config settings back in file
    for setting in config_settings:
        file.write(str(setting) + '\n')
    file.close()

    quit_now = input('Would you like to quit? Enter "-1" to do so. Otherwise, enter any character. ')
    if quit_now == '-1': break
