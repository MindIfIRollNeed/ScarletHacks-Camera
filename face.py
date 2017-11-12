import cognitive_face as CF
from firebase import firebase
import cv2
import json
import pprint
from datetime import datetime

KEY = '3c250b66b49d4b64b86afdca5d80c640'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'

CF.BaseUrl.set(BASE_URL)

img_url = 'test.png'

cap = cv2.VideoCapture(0)

# Saves picture taken to img_url
def fetchFrame():
    _, frame = cap.read()
    _, frame = cap.read()
    cv2.imwrite(img_url, frame)

def fetchFace():
    result = CF.face.detect(img_url, attributes='age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup')
    return result

if __name__ == '__main__':
    fetchFrame()
    result = fetchFace()[0]
    result['date'] = datetime.now().isoformat()
    try: 
        firebase = firebase.FirebaseApplication('https://scarlethacks-e6978.firebaseio.com')
        res = firebase.post('/users', result)
        print(res)
    except Exception as e:
        print(str(e))
