import requests
import argparse

parser = argparse.ArgumentParser(description='HDSky registers to check')
parser.add_argument('--apikey', '-k', help='Telegram api key')
parser.add_argument('--chatid', '-i', help='Telegram api key')
args = parser.parse_args()


def SendMessageToTelegram(msgText: str):
    post_dict = {'apiKey': args.apikey, 'chatId': args.chatid, 'msgText': msgText}
    requests.post(url='https://api.chancel.me/rest/api/v1/telegram', json=post_dict)


try:
    response = requests.get(url='https://hdsky.me/signup.php', timeout=30)
    if '自由注册当前关闭' not in response.text:
        SendMessageToTelegram('[HDSky]开放注册啦！')
except Exception as e:
    SendMessageToTelegram('检测[HDSky]注册检测发生异常，异常信息->%s' % str(e))

try:
    response = requests.get(url='https://chdbits.co/signup.php', timeout=30)
    if '自由注册当前关闭' not in response.text:
        SendMessageToTelegram('[chdbits]开放注册啦！')
except Exception as e:
    SendMessageToTelegram('检测[chdbits]注册检测发生异常，异常信息->%s' % str(e))

try:
    response = requests.get(url='https://ourbits.club/signup.php', timeout=30)
    if '自由注册当前关闭' not in response.text:
        SendMessageToTelegram('[ourbits]开放注册啦！')
except Exception as e:
    SendMessageToTelegram('检测[ourbits]注册检测发生异常，异常信息->%s' % str(e))

try:
    response = requests.get(url='https://hdhome.org/signup.php', timeout=30)
    if '自由注册当前关闭' not in response.text:
        SendMessageToTelegram('[hdhome]开放注册啦！')
except Exception as e:
    SendMessageToTelegram('检测[hdhome]注册检测发生异常，异常信息->%s' % str(e))
