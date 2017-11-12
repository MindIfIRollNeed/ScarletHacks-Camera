import cognitive_face as CF
from firebase import firebase
import pygame
import pygame.camera
from pygame import mixer
import json
import pprint
from datetime import datetime
import time
import rover

KEY = '3c250b66b49d4b64b86afdca5d80c640'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'

CF.BaseUrl.set(BASE_URL)

img_url = 'test.png'
pygame.camera.init()
mixer.init()
cam = pygame.camera.Camera("/dev/video0", (640,480))
cam.start()
rover.setupPins()
firebase = firebase.FirebaseApplication('https://scarlethacks-e6978.firebaseio.com')

# Saves picture taken to img_url
def fetchFrame():
    img = cam.get_image()
    pygame.image.save(img, img_url)

def fetchFace():
    result = CF.face.detect(img_url, attributes='age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup')
    return result

def processFace():
    fetchFrame()
    result = fetchFace()
    print(result)
    if len(result) == 0:
        return 
    result = result[0]
    try:
        if result['faceAttributes']['emotion']['happiness'] < 50:
            print('low happiness')
            rover.dispense()
            mixer.music.load('candy_georgie.mp3')
            mixer.music.play()
        res['date'] = datetime.now().isoformat()
        print(res)
        r = firebase.post('/users', res)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    while True:
        processFace()
        time.sleep(3.5)
