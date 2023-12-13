import requests
import os
import re
cookie_value = os.getenv('COOKIE')

cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}

headers = {
    'authority': 'www.north-plus.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': '_ga=GA1.2.1154037468.1702389658; _gid=GA1.2.1596932635.1702389658; eb9e6_lastpos=other; peacemaker=1; eb9e6_cknum=BAQDBVANUAZVDGw4B1NdAAkAUAoLVFIMWwJVXwYAAgABUQxUUApQAwcMB1c%3D; eb9e6_ck_info=%2F%09; eb9e6_winduser=BAcGD1cEWj9QAFMCAFUOAF4KBQEDBlEEA1QEWFQAVwZcBlwLBQJWUmo%3D; eb9e6_lastvisit=0%091702456847%09%2Fplugin.php%3FH_name-tasks.html.html; eb9e6_ol_offset=141135; _gat=1; _ga_RN4S7RB1LB=GS1.2.1702456853.3.0.1702456853.0.0.0',
    'referer': 'https://www.north-plus.net/plugin.php?H_name-tasks.html.html',
    'sec-ch-ua': '"Chromium";v="109", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
}

params = {
    'H_name': 'tasks',
    'action': 'ajax',
    'actions': 'job',
    'cid': '15',
    'nowtime': '1702456871219',
    'verify': 'ca81e905',
}

response = requests.get('https://www.north-plus.net/plugin.php', params=params, cookies=cookies, headers=headers)

output = response.text

pattern = re.compile('[\u4e00-\u9fa5]+')  # 匹配中文字符的正则表达式模式

matches = pattern.findall(output)  # 找到所有匹配的中文字符

if len(matches) > 0:
    extracted_text = matches[0]
    print(extracted_text)
else:
    print("出错")