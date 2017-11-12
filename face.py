import cognitive_face as CF
from firebase import firebase
import cv2
import json
import pprint
from datetime import datetime
import time
import rover

KEY = '3c250b66b49d4b64b86afdca5d80c640'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'

CF.BaseUrl.set(BASE_URL)

# img_url = 'test.png'
img_url = 'http://sugarandsawdust.com/wp-content/uploads/2017/08/fa35b0eb43fa459f8c7b2e7dcdd00226.jpg'
cap = cv2.VideoCapture(0)

firebase = firebase.FirebaseApplication('https://scarlethacks-e6978.firebaseio.com')

# Saves picture taken to img_url
def fetchFrame():
    _, frame = cap.read()
    _, frame = cap.read()
    cv2.imwrite(img_url, frame)

def fetchFace():
    result = CF.face.detect(img_url, attributes='age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup')
    return result

def processFace():
    # fetchFrame()
    result = fetchFace()
    for i, res in enumerate(result):
        try:
            if i == 0:
                if res['faceAttributes']['emotion']['happiness'] < 50:
                    rover.setupPins()
                    rover.dispense()
            res['date'] = datetime.now().isoformat()
            print(res)
            # r = firebase.post('/users', res)
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    while True:
        processFace()
        time.sleep(3.5)
