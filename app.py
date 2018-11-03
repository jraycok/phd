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
            bb=" kripik singkong"
        elif(a==2):
            b="anda membeli makroni pedas (4.000)"
            bb=" makroni pedas"
        elif(a==3):
            b="anda membeli makroni asin (4.000)"
            bb=" makroni asin"



        return {
                "speech": b+"\n"+"masukkan jumlah yang ingin anda pesan"+"\n"+"masukkan dengan menuliskan .0 dibagian akhir"+"\n"+"contoh memesan 2 : 2.0" ,
                "displayText": b+"\n"+"masukkan jumlah yang ingin anda pesan"+"\n"+"masukkan dengan menuliskan .0 dibagian akhir"+"\n"+"contoh memesan 2 : 2.0",
                #"data": {},
                #"contextOut": [],
                "source": b+"\n"+"masukkan jumlah yang ingin anda pesan"+"\n"+"masukkan dengan menuliskan .0 dibagian akhir"+"\n"+"contoh memesan 2 : 2.0"
            }

    if (req.get("result").get("action") == "jumlah"):
        a=req.get("result").get("resolvedQuery")
        aa=a.split(".")
        aaa=int(aa[0])
        
        total=aaa*4000
        
        return {
                "speech": "anda telah memesan"+str(a)+"bungkus dengan total harga "+str(total),
                "displayText": "anda telah memesan"+str(a)+"bungkus dengan total harga "+str(total),
                #"data": {},
                #"contextOut": [],
                "source": "anda telah memesan"+str(a)+"bungkus dengan total harga "+str(total),
            }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
