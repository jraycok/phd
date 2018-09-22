#!/usr/bin/env python


import json
import os
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
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
    if req.get("result").get("action") == "cek":
        driver = webdriver.PhantomJS();
        driver.get('https://www.phd.co.id/en/home#remodal-first')
        return {
            "speech": "tgl",
            "displayText": "tgl",
            #"data": {},
            #"contextOut": [],
            "source": "tgl"
        }
        #driver.find_element_by_link_text("Absensi Kuliah").click();
        #driver.find_element_by_id("txtUsername").send_keys("1")
        
        result0 = req.get("result")
        result1 = result0.get("resolvedQuery")
        result1 = result1.split("/")
        tgl = result1[0]
        bln = result1[1]
        thn = result1[2].split(" ")[0]
        lantai = result1[2].split(" ")[1]
        
        select = Select(driver.find_element_by_name("tgl"))
        select.select_by_value(tgl)
        select = Select(driver.find_element_by_name("bln"))
        select.select_by_value(bln)
        select = Select(driver.find_element_by_name("thn"))
        select.select_by_value(thn)
        select = Select(driver.find_element_by_name("lantai"))
        select.select_by_value(lantai)
        driver.find_element_by_name("cmd").click()


        soup = BeautifulSoup(driver.page_source,'html.parser')
        x = soup.find_all("tbody")
        tempat = str(x[9]).split("<tr>")[4]
        w = tempat.split("<tbody>")[1]
        #tempat
        r=[]
        i=2
        while i<27:
            r.append(w.split(">")[i].split("<")[0])
            i=i+2


        jadwal =[]


        #7.00 - 7.30
        loop=5
        while loop<31:
            p1 = str(x[9]).split("<tr>")[loop]
            jam = p1.split("</td>")[0].split('"')[12].split("<")[0].split(">")[1]
            i=0
            while i<13:
                try:
                    row = p1.split("</td>")[i].split('"')
                    if (len(row)>3):
                        if row[3]=="#FFCC66":
                            SKS = int(row[7])/2
                            ruangan = r[i]
                            kode = row[10].split("<")[0].split(">")[1]
                            if len(row)>12:
                                dosen = row[12].split("<")[0].split(">")[1]
                                jadwal.append(kode+"\n"+dosen+" ("+str(SKS)+" SKS"+")\n"+ruangan+"\n"+jam)
                            else:
                                jadwal.append(kode+"\n"+" ("+str(SKS)+" SKS"+")\n"+ruangan+"\n"+jam)
                    i=i+1
                except Exception as res:
                    i=i+1
            loop=loop+1

        hasil=""
        loop=0
        while loop<len(jadwal):
            hasil = hasil + jadwal[loop] + "\n\n"
            loop = loop+1
            
        return {
            "speech": hasil,
            "displayText": hasil,
            #"data": {},
            #"contextOut": [],
            "source": hasil
        }

                    
    
    

if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
