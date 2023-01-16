import requests
import json

import os
os.system('cls')

#########################################################################
api_request = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false")
api = json.loads(api_request.content)
#request made to the Api
#Then we parse the info thru jason
print(api)
currencies = ["eth","usdc","busd","btc"]
# to print(api)
#collecting what you want in a variable 
#running a loop to get stuff from what is returned from the Api
#then run another loop to get what you want from the variable


#My Portfolio 
my_portfolio = [
    {
    "sym":"btc",
    "amount_owned": 3000,
    "price_paid_per": .80
    },
    {
    "sym":"eth",
    "amount_owned": 5000,
    "price_paid_per": .20
    },
    {
    "sym":"busd",
    "amount_owned": 2000,
    "price_paid_per": .10
    },
        {
    "sym":"usdc",
    "amount_owned": 1000,
    "price_paid_per": 2.00
    }
    
    
    
    ]

print("--------------------------------------------")

# for x in api:
#     #print(x)
#     for coin in currencies:
#         #print(coin)
#         if coin == x["symbol"]:
#             print(x["name"])
#             print("$",x["current_price"])
#             print("Rank:",x["market_cap_rank"])

#print(x["name"])


for x in api:
    #print(x)
    for coin in my_portfolio:
        #print(coin)
        if coin['sym'] == x["symbol"]:
            print(x["name"])
            print("$",x["current_price"])
            print("Rank:",x["market_cap_rank"])

    