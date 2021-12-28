import requests
import argparse

parser = argparse.ArgumentParser(description='HDSky registers to check')
parser.add_argument('--apikey', '-k', help='Telegram api key')
parser.add_argument('--chatid', '-i', help='Telegram api key')
args = parser.parse_args()

response = requests.get(url='https://hdsky.me/signup.php')
if '自由注册当前关闭' not in response.text:
    post_dict = {
        'apiKey':args.apikey,
        'chatId':args.chatid,
        'msgText':'[HDSky]开放注册啦！'
    }
    requests.post(url='https://api.chancel.me/rest/api/v1/telegram',json=post_dict)