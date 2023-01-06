from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def request_code():
    
    headers = {
            'Content-type': 'application/json'
        }
            
    params = {
            'type': 's',
            'device_id': 'healthcheck'
        }
    
    url1 = 'https://www.naver.com'
    url2 = 'https://uremocon.com/pairing/getPairingList'
    
    response1 = requests.post(url1, headers=headers, params=params, verify=False)    
    response2 = requests.post(url2, headers=headers, params=params, verify=False)
    
    state1 = response1.status_code
    state2 = response2.status_code
    
    return render_template("index.html", url1=url1, url2=url2, state1=state1, state2=state2)
          

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)