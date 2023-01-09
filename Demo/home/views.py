
from django.shortcuts import render,HttpResponse
import face_recognition
import numpy as np
from PIL import Image
import IPython.display as display
import cv2
from keras.models import load_model
import os
import base64
from stonks_index import views
import json


 
def home(request):
    return render(request, 'home/home.html')

def base(request):
    resultTemp = request.POST.get('basefile')
    result = resultTemp.split(',')[1]
    # base64解码(解成二进制串)
    decode_jpg = base64.b64decode(result)
    # print(decode_jpg)
    # 写入jpg文件
    with open('./output/new.jpg', 'wb') as f:
        f.write(decode_jpg)
    response = process()
    return render(request, 'home/upload.html', {'result': response})

def test(request):

    jsonStr = json.loads(views.test_api())
    print(jsonStr[0][0])
    return render(request, 'home/result.html', {'result': jsonStr[0][0]})

def upload(request):
    return render(request, 'home/upload.html')
    
def analysis(request):
    resArr = views.test_api()
    print(resArr)
    #'joy_all':resArr[0], 'shocked_all':resArr[1], 'neutral_all':resArr[2], 'hate_all':resArr[3], 'sad_all':resArr[4], 'angrt_all':resArr[5],'amazed_all':resArr[6]
    return render(request, 'home/analysis.html', {'joy_all':resArr[0], 'shocked_all':resArr[1], 'neutral_all':resArr[2], 'hate_all':resArr[3], 'sad_all':resArr[4], 'angrt_all':resArr[5],'amazed_all':resArr[6], 'joy_man':resArr[7], 'shocked_man':resArr[8], 'neutral_man':resArr[9], 'hate_man':resArr[10], 'sad_man':resArr[11], 'angrt_man':resArr[12],'amazed_man':resArr[13],'joy_woman':resArr[14], 'shocked_woman':resArr[15], 'neutral_woman':resArr[16], 'hate_woman':resArr[17], 'sad_woman':resArr[18], 'angrt_woman':resArr[19],'amazed_woman':resArr[20],'joy_PR':resArr[21], 'shocked_PR':resArr[22], 'neutral_PR':resArr[23], 'hate_PR':resArr[24], 'sad_PR':resArr[25], 'angrt_PR':resArr[26],'amazed_PR':resArr[27],'joy_IT':resArr[28], 'shocked_IT':resArr[29], 'neutral_IT':resArr[30], 'hate_IT':resArr[31], 'sad_IT':resArr[32], 'angrt_IT':resArr[33],'amazed_IT':resArr[34],'joy_HR':resArr[35], 'shocked_HR':resArr[36], 'neutral_HR':resArr[37], 'hate_HR':resArr[38], 'sad_HR':resArr[39], 'angrt_HR':resArr[40],'amazed_HR':resArr[41]})

    

def process():
    angry=0
    sad=0
    neutral=0
    hate=0
    shocked=0
    fear=0
    joy=0

    emotion_dict= {'生氣': 0, '悲傷': 5, '中性': 4, '厭惡': 1, '驚訝': 6, '恐懼': 2, '高興': 3}

    def face_rec(path):
        angry=0
        sad=0
        neutral=0
        hate=0
        shocked=0
        fear=0
        joy=0
        image = face_recognition.load_image_file(path)
        # 載入影像

        face_locations = face_recognition.face_locations(image)
        # 尋找臉部

        top, right, bottom, left = face_locations[0]
        # 將臉部框起來

        face_image = image[top:bottom, left:right]
        face_image = cv2.resize(face_image, (48,48))
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])
        # 調整到可以進入該模型輸入的大小

        model = load_model("C:/Users/K/Downloads/djangoXcopy-20221127T142618Z-001/djangoXcopy/Demo/home/model/model_v6_23.hdf5")
        # 載入模型

        predicted_class = np.argmax(model.predict(face_image))
        # 分類情緒

        label_map = dict((v,k) for k,v in emotion_dict.items()) 
        predicted_label = label_map[predicted_class]
        # 根據情緒對映表輸出情緒

        print(predicted_label)
        if predicted_label=="生氣":
            angry+=1
            return "angry"
        elif predicted_label=="悲傷":
            sad+=1
            return "sad"
        elif predicted_label=="中性":
            neutral+=1
            return "neutral"
        elif predicted_label=="厭惡":
            hate+=1
            return "hate"
        elif predicted_label=="驚訝":
            shocked+=1
            return "shocked"
        elif predicted_label=="恐懼":
            fear+=1
            return "fear"
        else:
            joy+=1
            return "joy"

        display.display(Image.open(path))
        print("------------------------------------------------------------------------------------------------------------")
    Path = "C:/Users/K/Downloads/djangoXcopy-20221127T142618Z-001/djangoXcopy/Demo/output/"
    allFileList = os.listdir(Path)
    #讀取目標資料夾路徑
    for file in allFileList:
        if os.path.isdir(os.path.join(Path,file)):
            print("I'm a directory: " + file)
        elif os.path.isfile(Path+file):
            return face_rec(Path+file)
        else:
            print('OH MY GOD !!') 
    # #以迴圈讓每個檔案呼叫function
    # print("各自情緒加總:",angry,sad,neutral,hate,shocked,fear,joy)
