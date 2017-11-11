# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:27:47 2017

@author: sarah
"""

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys

key = '44be13f4f58c4bdfb18a4d9ffd8716c1'

content= input("url or file?:")

if content=='url':
    urlname = input("enter url:")
    headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': key,
    }
    
    body = "{ 'url': '"+ urlname +"' }"

        
        
else:
    filepath = input("path of file:")
    
    headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': key,
    }
    
    body = open(filepath,'rb').read()

params = urllib.parse.urlencode({
    })
    
try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e.args)

####################################