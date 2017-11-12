# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Sat Nov 11 15:27:47 2017

@author: sarah
"""

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import cv2
import json

cap = cv2.VideoCapture(0)

filepath = 'test.png'

key = '44be13f4f58c4bdfb18a4d9ffd8716c1'

class Emotions:
    def __init__(self, emotions):
        scores = emotions['scores']
        self.anger = scores['anger']
        self.contempt = scores['contempt']
        self.disgust = scores['disgust']
        self.fear = scores['fear']
        self.happiness = scores['happiness']
        self.neutral = scores['neutral']
        self.sadness = scores['sadness']
        self.surprise = scores['surprise']

# Saves picture taken to filepath
def fetchFrame():
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    cv2.imwrite(filepath, frame)

# Sends request to microsoft emotions api and returns emotion values
def fetchEmotions():
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': key,
    }

    try:
        body = open(filepath,'rb').read()
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize", body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print(e.args)
    return None

####################################

if __name__ == "__main__":
    fetchFrame()
    emotions = fetchEmotions()
    e = Emotions(json.loads(emotions)[0])
    print(e.sadness)
