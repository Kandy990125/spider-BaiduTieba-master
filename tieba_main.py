from get_sign_num import sign_num_main
from SQL_main import insert_sql
import datetime
import time
import requests
import re
def get_focus_comment_num(kw):
    html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=%s&fr=search' % (kw)).content
    pattern1 = re.compile('<span class="card_menNum">(.*?)</span>', re.S)
    focus_num = int(re.search(pattern1, html.decode('utf-8')).group(1).replace(',',''))
    pattern2 = re.compile('<span class="card_infoNum">(.*?)</span>', re.S)
    comment_num = int(re.search(pattern2, html.decode('utf-8')).group(1).replace(',', ''))
    return focus_num, comment_num

def main():
    sign_num_list = sign_num_main()
    for item in sign_num_list:
        kw = item['kw']
        sign_num = item['sign_num']
        focus_num, comment_num = get_focus_comment_num('蔡徐坤')
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        insert_sql('BaiduTieba', kw, time, comment_num, focus_num, sign_num)

if __name__ =="__main__":
    while True:
        hour = int(datetime.datetime.now().strftime('%H'))
        minute = int(datetime.datetime.now().strftime('%M'))
        if minute == 55 and hour == 23 :
            main()
        time.sleep(60)