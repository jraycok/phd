#!/usr/bin/env python

import urllib
import json
import os
import requests

import math



from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])


def webhook():
    req = request.get_json(silent=True, force=True)
    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'

    return r




def makeWebhookResult(req):
    if (req.get("result").get("action") == "pilihsnacknya"):
        a=req.get("result").get("resolvedQuery")
        a=int(a)
        if(a==1):
            b="anda membeli kripik singkong (4.000)"
        elif(a==2):
            b="anda membeli makroni pedas (4.000)"
        elif(a==3):
            b="anda membeli makroni asin (4.000)"

        


    return {
            "speech": b+"\n"+"masukkan jumlah yang ingin anda pesan"+"\n"+"masukkan dengan menuliskan 0. dahulu"+"\n"+"contoh memesan 2 : 0.2" ,
            "displayText": b+"\n"+"masukkan jumlah yang ingin anda pesan"+"\n"+"masukkan dengan menuliskan 0. dahulu"+"\n"+"contoh memesan 2 : 0.2",
            #"data": {},
            #"contextOut": [],
            "source": b+"\n"+"masukkan jumlah yang ingin anda pesan"+"\n"+"masukkan dengan menuliskan 0. dahulu"+"\n"+"contoh memesan 2 : 0.2"
        }



if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
