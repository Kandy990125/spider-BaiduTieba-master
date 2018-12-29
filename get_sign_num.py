import requests
import json
import random
headers = {
        'Host': 'tieba.baidu.com',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    }
def get_cookies():
    COOKIES = []
    with open("cookies1.txt", 'r', encoding='utf-8') as f:
        list = f.readlines()
        for item in list:
            item_list = item.split('----')
            COOKIES.append(item_list[4][:-1])
        return COOKIES

def get_cookie():
    cookies_list = get_cookies()
    i = random.randint(0, len(cookies_list) - 1)
    Cookie = cookies_list[i]
    return i, Cookie


def item_sign(kw, cookie):
    headers['Cookie'] = cookie
    response = requests.get('http://tieba.baidu.com/dc/common/tbs', headers=headers)
    tbs = json.loads(response.text)['tbs']
    data = {
            'ie': 'utf-8','kw': kw,'tbs': tbs,
        }
    url = 'http://tieba.baidu.com/sign/add'
    req = requests.post(url, headers=headers, data=data)
    url = "http://tieba.baidu.com/sign/loadmonth?kw=%s&ie=utf-8"% (kw)
    response = requests.get(url, headers=headers)
    sign_num = json.loads(response.content)['data']['sign_user_info']['rank']
    result_data = {
        'kw':kw,
        'sign_num':sign_num
    }
    return result_data

def sign_num_main():
    kw_list = ['蔡徐坤' ,'陈立农','范丞丞', '黄明昊', '林彦俊', '朱正廷', '王子异' , '王琳凯', '尤长靖']
    result_list = []
    for kw in kw_list:
        print(kw)
        while True:
            i, cookie = get_cookie()
            try:
                result  = item_sign(kw, cookie)
                result_list.append(result)
                print(kw,result)
                break
            except:
                with open('error_account.txt', 'a') as f:
                    f.write(str(i) + " " + cookie + "\n")
    return result_list