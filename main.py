from dadata import Dadata
from pyrogram import Client


api_id = 25598825
api_hash = '90c582eb762a278430d8e7785f165cdc'
bot_token = '6074317523:AAEY2v7UGTTOwMNLHTh6Jfvfg3wKmcbnSDo'

app = Client("my_account", api_id=api_id, api_hash=api_hash)


# token = '0ef89a6c404a3faa24a15fa6ffe8715450f8ee91'
# dadata = Dadata(token)
#
# inputt = input("введите запрос")
# result = dadata.suggest("address", inputt)
#
#
# while len(result) > 1:
#     for i in range(len(result)):
#         print(result[i]["value"])
#
#     choice = int(input("выберите"))
#
#     result = dadata.suggest("address", result[choice - 1]['value'])
# print(result[0]['value'])
# print(result[0]['data']['geo_lat'])
# print(result[0]['data']['geo_lon'])

