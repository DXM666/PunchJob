import requests
import json
import datetime

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
account_login = requests.post(
    url='https://www.xybsyw.com/json/wx/studentclock/bindAccount.xhtml?username=17854400796&password=wei123456'
    , verify=False, headers=headers
)
user_id = json.loads(account_login.text)['uid']

get_item = requests.post(
    url='https://www.xybsyw.com/json/wx/studentclock/planList.xhtml?uid=' + str(user_id) + '&type=1')
item_id = json.loads(get_item.text)['datas'][0]['planId']


punch_end = requests.post(url='https://www.xybsyw.com/json/wx/studentclock/updateClock.xhtml',
                          data={'uid': user_id, 'reason': '', 'traineeId': item_id, 'lng': 120.513986,
                                'lat': 36.858314,'address':'山东省青岛市莱西市水集街道','clockType':1,'punchInStatus':0,'clockDate':datetime.datetime.now().strftime('%Y-%m-%d')})
if json.loads(punch_end.text)['success']:
    print('Punch Success!')
else:
    print('Punch False!')