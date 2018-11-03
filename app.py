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
            b="anda membeli kripik singkong"
        elif(a==2):
            b="anda membeli makroni pedas"
        elif(a==3):
            b="anda membeli makroni asin"

        


    return {
            "speech": b+"\n"+"masukkan jumlah",
            "displayText": b+"\n"+"masukkan jumlah",
            #"data": {},
            #"contextOut": [],
            "source": b+"\n"+"masukkan jumlah"
        }



if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
