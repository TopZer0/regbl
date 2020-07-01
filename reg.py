import requests
import json
from requests.auth import HTTPBasicAuth
import urllib.parse

for x in range(0,100):
    stop = False
    while (stop == False):
        NomerHp = str(input('Input Nomer HP : '))
        response = requests.get('https://randomuser.me/api/?gender=male&nat=us')
        resp = response.text
        AndroidId = json.loads(resp).get('info').get('seed')
        useName = json.loads(resp).get('results')[0].get('login').get('username')
        userName = useName+'zas'
        NamaAkun = json.loads(resp).get('results')[0].get('name').get('first')+' Rahmat'
        uuId = json.loads(resp).get('results')[0].get('login').get('uuid')

        headers = {
            'Host': 'accounts.bukalapak.com',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
            'x-user-id': '-1',
            'x-device-ad-id': '',
            'bukalapak-identity': AndroidId,
            'accept': 'application/json',
            'bukalapak-app-version': '4040204',
            'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
            'conversion-tracking-params': '5.1.1 22 4.40.4',
            'content-type': 'application/x-www-form-urlencoded',
        }

        data = 'client_id=40349e6a0eedaa0e7561a494' \
               '&client_secret=53b6ddb9216f33fb2d62998760995eb948c7c0f6486d50aea5509f83cf504f3a' \
               '&grant_type=client_credentials' \
               '&scope=public'

        response = requests.post('https://accounts.bukalapak.com/oauth/token', headers=headers, data=data)
        resp = response.text
        bearer = json.loads(resp).get('access_token')
        print(bearer)
        headers = {
            'Host': 'api.bukalapak.com',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
            'x-user-id': '-1',
            'x-device-ad-id': uuId,
            'bukalapak-identity': AndroidId,
            'accept': 'application/json',
            'bukalapak-app-version': '4040204',
            'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
            'conversion-tracking-params': '5.1.1 22 4.40.4',
            'authorization': 'Bearer '+bearer,
        }

        params = (
            ('name', NamaAkun),
        )

        response = requests.get('https://api.bukalapak.com/_exclusive/users/registration-availability', headers=headers, params=params)
        resp = response.text
        print(resp)
        if json.loads(resp).get('meta').get('http_status') == 200:
            params = (
                ('username', userName),
            )

            response = requests.get('https://api.bukalapak.com/_exclusive/users/registration-availability', headers=headers, params=params)
            resp = response.text
            print(resp)
            if json.loads(resp).get('meta').get('http_status') == 200:
                params = (
                    ('phone', NomerHp),
                )

                response = requests.get('https://api.bukalapak.com/_exclusive/users/registration-availability', headers=headers, params=params)
                resp = response.text
                print(resp)
                if json.loads(resp).get('meta').get('http_status') == 200:
                    headers = {
                        'Host': 'api.bukalapak.com',
                        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
                        'x-user-id': '-1',
                        'x-device-ad-id': uuId,
                        'identity': AndroidId,
                        'appversion': '4040204',
                        'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
                        'conversion-tracking-params': '5.1.1 22 4.40.4',
                        'content-type': 'application/x-www-form-urlencoded',
                    }

                    data = 'identity=&manual_phone='+NomerHp+\
                           '&feature=phone_registration'

                    response = requests.post('https://api.bukalapak.com/v2/trusted_devices/device_need_validation.json', headers=headers, data=data)
                    resp = response.text
                    print(resp)
                    if json.loads(resp).get('status') == 'OK':
                        headers = {
                            'Host': 'api.bukalapak.com',
                            'bukalapak-otp-method': 'sms',
                            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
                            'x-user-id': '-1',
                            'x-device-ad-id': uuId,
                            'identity': AndroidId,
                            'appversion': '4040204',
                            'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
                            'conversion-tracking-params': '5.1.1 22 4.40.4',
                            'content-type': 'application/x-www-form-urlencoded',
                        }

                        data = 'identity='+AndroidId+\
                               '&feature=phone_registration&manual_phone='+NomerHp+\
                               '&feature_tag=phone_registration'

                        response = requests.post('https://api.bukalapak.com/v2/trusted_devices/otp_request.json', headers=headers, data=data)
                        resp = response.text
                        print(resp)
                        if json.loads(resp).get('status') == 'OK':
                            stop = True
                else:
                    print('Nomer Sudah Didaftarkan')
            else:
                print('UserName Sudah diGunakan')


    while True:
        headers = {
            'Host': 'api.bukalapak.com',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
            'x-user-id': '-1',
            'x-device-ad-id': uuId,
            'identity': AndroidId,
            'appversion': '4040204',
            'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
            'conversion-tracking-params': '5.1.1 22 4.40.4',
            'content-type': 'application/x-www-form-urlencoded',
        }
        Otp = str(input('OTP Nomer 1 : '))
        data = 'otp='+Otp+\
               '&identity='+AndroidId+\
               '&feature=phone_registration'\
               '&manual_phone='+NomerHp+\
               '&feature_tag=phone_registration'

        response = requests.post('https://api.bukalapak.com/v2/trusted_devices.json', headers=headers, data=data)
        resp = response.text
        if json.loads(resp).get('status') == 'OK':
            data = 'user%5Bemail%5D='+NomerHp+ \
                   '&user%5Busername%5D='+userName+ \
                   '&user%5Bname%5D='+NamaAkun+ \
                   '&user%5Bpassword%5D=t3rs3r4h' \
                   '&user%5Bpassword_confirmation%5D=t3rs3r4h' \
                   '&user%5Bpolicy%5D=1' \
                   '&user%5Bgender%5D=Laki-laki' \
                   '&user%5Breferral_as_buyer%5D=false' \
                   '&source=bukalapak' \
                   '&facebook%5Btoken%5D=' \
                   '&facebook%5Buid%5D=' \
                   '&google%5Btoken%5D='

            response = requests.post('https://api.bukalapak.com/v2/users/register.json', headers=headers, data=data)
            resp = response.text
            if json.loads(resp).get('status') == 'OK':
                userId=str(json.loads(resp).get('user_id'))
                token=json.loads(resp).get('token')
                headers = {
                    'Host': 'api.bukalapak.com',
                    'cache-control': 'public, max-stale=2419200',
                    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
                    'x-user-id': userId,
                    'x-device-ad-id': uuId,
                    'identity': AndroidId,
                    'appversion': '4040204',
                    'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
                    'conversion-tracking-params': '5.1.1 22 4.40.4',
                }
                response = requests.get('https://api.bukalapak.com/v2/users.json', headers=headers,auth=HTTPBasicAuth(userId, token))
                resp = response.text
                if json.loads(resp).get('status') == 'OK':
                    headers = {
                        'Host': 'accounts.bukalapak.com',
                        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
                        'x-user-id': userId,
                        'x-device-ad-id': uuId,
                        'bukalapak-identity': AndroidId,
                        'accept': 'application/json',
                        'bukalapak-app-version': '4040204',
                        'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
                        'conversion-tracking-params': '5.1.1 22 4.40.4',
                        'authorization': 'Bearer '+bearer,
                        'content-type': 'application/x-www-form-urlencoded',
                    }

                    data = 'client_id=40349e6a0eedaa0e7561a494' \
                           '&client_secret=53b6ddb9216f33fb2d62998760995eb948c7c0f6486d50aea5509f83cf504f3a' \
                           '&grant_type=password' \
                           '&scope=public%20user%20store' \
                           '&username='+userId+ \
                           '&password='+token

                    response = requests.post('https://accounts.bukalapak.com/oauth/token', headers=headers, data=data)
                    resp = response.text
                    accessToken = json.loads(resp).get('access_token')
                    headers = {
                        'Host': 'api.bukalapak.com',
                        'if-none-match': '',
                        'bukalapak-otp-method': 'sms',
                        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
                        'x-user-id': userId,
                        'x-device-ad-id': uuId,
                        'identity': AndroidId,
                        'appversion': '4040204',
                        'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
                        'conversion-tracking-params': '5.1.1 22 4.40.4',
                    }

                    response = requests.get('https://api.bukalapak.com/v2/users/tfa-status.json', headers=headers,auth=HTTPBasicAuth(userId, token))
                    resp = response.text
                    if json.loads(resp).get('data').get('tfa_status') == True:
                        data = 'identity='+AndroidId+'&feature=global&feature_tag=deactivate_tfa'
                        response = requests.post('https://api.bukalapak.com/v2/trusted_devices/otp_request.json', headers=headers, data=data,auth=HTTPBasicAuth(userId, token))
                        break
        else:
            print('OTP 1 SALAH')

    while True:
        headers = {
            'Host': 'api.bukalapak.com',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
            'x-user-id': userId,
            'x-device-ad-id': uuId,
            'identity': AndroidId,
            'appversion': '4040204',
            'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
            'conversion-tracking-params': '5.1.1 22 4.40.4',
            'content-type': 'application/x-www-form-urlencoded',
        }
        OTp2 = str(input('OTP Nomer 2 : '))
        data = 'otp='+OTp2+'&identity='+AndroidId+'&feature=global&feature_tag=deactivate_tfa'

        response = requests.post('https://api.bukalapak.com/v2/trusted_devices.json', headers=headers, data=data,auth=HTTPBasicAuth(userId, token))
        resp = response.text
        if json.loads(resp).get('status') == 'OK':
            headers = {
                'Host': 'api.bukalapak.com',
                'if-none-match': '',
                'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G930L Build/NRD90M) 4040204 BLAndroid BLMobile/4040204',
                'x-user-id': userId,
                'x-device-ad-id': uuId,
                'identity': AndroidId,
                'appversion': '4040204',
                'ad-user-agent': 'com.bukalapak.android/4.40.4 (Android 5.1.1; en_ID; SM-G930L; Build/NRD90M)',
                'conversion-tracking-params': '5.1.1 22 4.40.4',
            }
            response = requests.patch('https://api.bukalapak.com/v2/users/tfa-status.json', headers=headers,auth=HTTPBasicAuth(userId, token))
            resp = response.text
            if json.loads(resp).get('data').get('tfa_status') == False:
                print(NomerHp,'Registrasi Berhasil')
                break
        else:
            print('OTP 2 SALAH')








