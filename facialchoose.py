# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Sat Nov 11 15:27:47 2017

@author: sarah
"""

import http.client
import urllib.request
import urllib.parse
import urllib.error
import requests
import base64
import sys
import json
import cv2

cap = cv2.VideoCapture(0)

filepath = 'test.png'

emotions_key = '44be13f4f58c4bdfb18a4d9ffd8716c1'
face_key = '3c250b66b49d4b64b86afdca5d80c640'

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
        'Ocp-Apim-Subscription-Key': emotions_key,
    }

    try:
        body = open(filepath,'rb').read()
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize", body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print(e.args)
    return None

# Sends request to microsfot face api and returns faces api
def fetchFace():
    uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

    # Request headers.
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': face_key,
    }

    # Request parameters.
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    # Body. The URL of a JPEG image to analyze.
    body = {'url': 'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}

    try:
        # Execute the REST API call and get the response.
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)

        print ('Response:')
        parsed = json.loads(response.text)
        print (json.dumps(parsed, sort_keys=True, indent=2))

    except Exception as e:
        print('Error:')
        print(e)

if __name__ == "__main__":
    fetchFrame()
    # emotions = fetchEmotions()
    # e = Emotions(json.loads(emotions)[0])
    # print(e.sadness)
    face = fetchFace()
    print(face)
