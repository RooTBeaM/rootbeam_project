from binance.client import Client
import keys
import pprint

client = Client(keys.API_key, keys.Secret_key)


try:
    print('==========='*10)
    print('Future Account Balancce')
    for i in client.futures_account_balance():
        if round(float(i['balance']),4) != 0:
            print(i)
    balance_USDT = round(float(client.futures_account_balance()[6]['balance']),2)
    print('balance_USDT =',balance_USDT)
    print('==========='*10)
except:
    print('Binance Invalid API Key ....')

try:
    print('==========='*10)
    print('Margin Account Balancce')
    for i in client.get_margin_account()['userAssets']:
        if round(float(i['free']),4) != 0:
            print(i)
    print('==========='*10)
except:
    print('Binance Invalid API Key ....')

try:
    print('==========='*10)
    print('Spot Account Balancce')
    for i in client.get_account()['balances']:
        if round(float(i['free']),4) != 0:
            print(i)
except:
    print('Binance Invalid API Key ....')
