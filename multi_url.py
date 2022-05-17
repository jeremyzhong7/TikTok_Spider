import re
import uuid
import requests
import os
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36'
}


def getUrl(shareUrl):
    # 分享up主的临时地址
    url = shareUrl

    res = requests.get(url=url, headers=headers, allow_redirects=False)
    # print(res.headers['Location'])
    sec_uid = re.search(r'/user/(.*)\?', res.headers['Location']).group(1)
    print("get sec_uid successfully，sec_uid：{}".format(sec_uid))

    if os.path.exists('json/{}'.format(sec_uid)) is False:
        os.mkdir('json/{}'.format(sec_uid))

    params = {
        # 每次请求的数量
        'count': 14,
        # 参数 判断第几页
        'max_cursor': 0,
        'has_more': True
    }

    cnt = 0
    while params['has_more']:
        # 视频所有资料
        aweme_list = []
        # 获取用户视频链接信息
        listURL = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid={}&count={}&max_cursor={}'.format(sec_uid, params['count'], params['max_cursor'])

        response = requests.get(url=listURL, headers=headers)
        if response.status_code == 200 and response.json()['status_code'] == 0:
            jsondata = response.json()
            params['has_more'] = jsondata['has_more']
            params['max_cursor'] = jsondata['max_cursor']
            aweme_list = jsondata['aweme_list']
            # print("url: {}".format(listURL))
            # print("list itemCount: {}".format(len(aweme_list)))
            # print("has_more: {}".format(params['has_more']))

            if len(aweme_list) > 0:
                with open('./json/{}/{}.json'.format(sec_uid, uuid.uuid1().hex), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(jsondata))
                    f.close()
                    cnt += 1
                    print("Spider {} Page, filename: {}".format(cnt, f.name))
    return sec_uid
