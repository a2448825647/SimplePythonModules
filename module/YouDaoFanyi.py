import json
import requests
import time
import random
import hashlib


def getMd5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding='Utf-8'))
    md5_str = md5.hexdigest()
    return md5_str

def get_translate_date(e):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    r = "" + str((time.time() * 1000))
    i = r + str(random.randint(0,10))
    to_salt = i
    to_sign = getMd5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
    to_ts = r
    #谷歌浏览器某版本md5
    to_bv = '6bd43b532a04b6145782cfe65196ca4f'



    form_data = {}
    # 需要翻译的文字
    form_data['i'] = e
    # 下面这些都先按照我们之前抓包获取到的数据
    form_data['from'] = 'AUTO'
    form_data['to'] = 'AUTO'
    form_data['smartresult'] = 'dict'
    form_data['client'] = 'fanyideskweb'
    form_data['salt'] = to_salt
    form_data['sign'] = to_sign
    form_data['ts'] = to_ts
    form_data['bv'] = to_bv
    form_data['doctype'] = 'json'
    form_data['version'] = '2.1'
    form_data['keyfrom'] = 'fanyi.web'
    form_data['action'] = 'FY_BY_REALTlME'


    headers ={
        'Accept': 'application/json, text/javascript, */*; q=0.01', \
        'Accept-Encoding': 'gzip, deflate', \
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8', \
        'Connection': 'keep-alive', \
        'Content-Length': '238', \
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', \
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1293870634@222.128.56.148; JSESSIONID=aaaQmWwIFXYcI45B_GW9w; OUTFOX_SEARCH_USER_ID_NCOO=859230941.8657871; ___rl__test__cookies=1578144246831', \
        'Host': 'fanyi.youdao.com', \
        'Origin': 'http://fanyi.youdao.com', \
        'Referer': 'http://fanyi.youdao.com/', \
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', \
        'X-Requested-With': 'XMLHttpRequest'
    }

    #form_data = urllib.parse.urlencode(form_data).encode('utf-8')
    response_data = requests.post(url = url,data = form_data,headers = headers)
    #把返回来的json字符串解析成字典
    if(len(response_data.text) > 0):
        print(response_data.text)
        result_dict = json.loads(response_data.text)
        #print(result_dict )
        print('翻译:' + result_dict['translateResult'][0][0]['tgt']+ '\n')
        if 'smartResult' in result_dict:
            print('相关结果：')
            size = len(result_dict['smartResult']['entries'])
            if size > 1:
               for x in range(1,len(result_dict['smartResult']['entries'])):
                   print(result_dict['smartResult']['entries'][x])
                   a = 0
while(1):
    #in_str = input('请输入：')
    get_translate_date(e = str(random.randint(0,100)))
