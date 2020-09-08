import base64
import hashlib
import hmac
import json
import time
import httplib2
import configparser

config = configparser.ConfigParser()
config.read('../conf/config.ini')
ACCESS_TOKEN = config['COINONE']['access_token']
SECRET_KEY = bytes(config['COINONE']['secret_key'], 'utf-8')

def get_encoded_payload(payload):
    payload['nonce'] = int(time.time() * 1000)

    dumped_json = json.dumps(payload)
    encoded_json = base64.b64encode(bytes(dumped_json, 'utf-8'))
    return encoded_json


def get_signature(encoded_payload):
    signature = hmac.new(SECRET_KEY, encoded_payload, hashlib.sha512)
    return signature.hexdigest()


def get_response(action, payload):
    url = '{}{}'.format('https://api.coinone.co.kr/', action)

    encoded_payload = get_encoded_payload(payload)

    headers = {
        'Content-type': 'application/json',
        'X-COINONE-PAYLOAD': encoded_payload,
        'X-COINONE-SIGNATURE': get_signature(encoded_payload),
    }

    http = httplib2.Http()
    response, content = http.request(url, 'POST', body=encoded_payload, headers=headers)

    return content


print(get_response(action='v2/account/balance', payload={
    'access_token': ACCESS_TOKEN,
}))