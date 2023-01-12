from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def request_code():
    
    headers = {
            'Content-type': 'application/json',
        }
    
    params = {
        'type': 's',
        'device_id': 'healthcheck',
    }
            
    json_data1 = {
    'stbModel': 'UIE4027LGU',
    'packageName': 'com.lguplus.iptv3.base.launcher',
    'isCVT': 'N',
    }
    
    json_data2 = {
    'stbModel': 'UHD4K',
    'subscriberNumber': 'M1294125121',
    'firmwareVersion': '',
    'osVersion': '29',
    'sbcType': '70002',
    }
    
    url1 = 'https://fluterepair.uplus.co.kr:8443/openapi/appinfo'
    url2 = 'https://fluterepair.uplus.co.kr:8443/openapi/appList'
    url3 = 'https://uremocon.com/pairing/getPairingList'
    url4 = 'https://google.com'
    
    response1 = requests.post(url1, headers=headers, json=json_data1, verify=False)
    response2 = requests.post(url2, headers=headers, json=json_data2, verify=False)    
    response3 = requests.get(url3, params=params, headers=headers, verify=False)
    
    state1 = response1.status_code
    state2 = response2.status_code
    state3 = response3.status_code
    
    text1 = response1.text
    text2 = str(response2.json())
    text3 = str(response3.json())
    
    return render_template("index.html", url1=url1, url2=url2, url3=url3, 
                           state1=state1, state2=state2, state3=state3,
                           text1=text1[10:14], text2=text2[11:15], text3=text3[10:14])


@app.route("/WAS1")
def response1():
    
    headers = {
            'Content-type': 'application/json',
        }
            
    json_data1 = {
    'stbModel': 'UIE4027LGU',
    'packageName': 'com.lguplus.iptv3.base.launcher',
    'isCVT': 'N',
    }
    
    url1 = 'https://fluterepair.uplus.co.kr:8443/openapi/appinfo'
    url4 = 'https://google.com'
    
    response1 = requests.post(url1, headers=headers, json=json_data1, verify=False)
    
    text1 = response1.text
    
    return render_template("response1.html", url1=url1, text1=text1)

@app.route("/WAS2")
def response2():
    
    headers = {
            'Content-type': 'application/json',
        }
            
    json_data2 = {
    'stbModel': 'UHD4K',
    'subscriberNumber': 'M1294125121',
    'firmwareVersion': '',
    'osVersion': '29',
    'sbcType': '70002',
    }
    
    url2 = 'https://fluterepair.uplus.co.kr:8443/openapi/appList'
    
    response2 = requests.post(url2, headers=headers, json=json_data2, verify=False)
    
    text2 = response2.json()
    
    return render_template("response2.html", url2=url2, text2=text2)

@app.route("/uremocon")
def response3():
    
    headers = {
            'Content-type': 'application/json',
        }
            
    params = {
        'type': 's',
        'device_id': 'healthcheck',
    }
    
    url3 = 'https://uremocon.com/pairing/getPairingList'
    
    response3 = requests.get(url3, params=params, headers=headers, verify=False)
    
    text3 = response3.json()
    
    return render_template("response3.html", url3=url3, text3=text3)
              
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)