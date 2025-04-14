import requests

cookies = {
    写你自己的
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'https://blog.csdn.net',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://blog.csdn.net/你的?type=sub&spm=你的',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

params = {
    'pageSize': '9999',
    'username': '你的',
}

def parse_followings(resp_json):
    following_list = []
    data_list = resp_json['data']['list']
    for data in data_list:
        following_list.append(data['username'])

    return following_list

def unFollow(follow):
    json_data = {
        'username': '你的', 
        'follow': follow,
        'source': 'ME',
        'fromType': 'pc',
        'detailSourceName': '个人主页',
    }
    response = requests.post('https://mp-action.csdn.net/interact/wrapper/pc/fans/v1/api/unFollow', cookies=cookies, headers=headers, json=json_data)
    print(f"取关用户{follow} -> " + response.text)

if __name__ == "__main__":
    response = requests.get('https://mp-action.csdn.net/interact/wrapper/pc/fans/v1/api/getFollowOffsetList', params=params, cookies=cookies, headers=headers)
    following_list = parse_followings(response.json())

    white_list = ['WhereIsHeroFrom', 'shipsail', 'u014727709']

    for user in following_list:
        if user not in white_list:  # 检查用户是否在白名单中
            unFollow(user)
        else:
            print(f"用户{user}在白名单内，不取关")

