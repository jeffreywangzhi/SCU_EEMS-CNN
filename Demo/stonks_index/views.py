from django.shortcuts import render
from django.http import JsonResponse #剛剛的JsonResponse套件
from stonks_index.models import DBTest #從models.py import DBTest 物件
from django.core import serializers

from django.db import models, connection
import json

class FoodManager(models.Manager):
    def get_120_food(self):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT name 
            FROM restaurants_food 
            WHERE price=120
        """)
        return [result[0] for result in cursor.fetchall()]
        
class Food(models.Model):
    ...
    objects = FoodManager()
    ...

def test_api():

    arr = []
    cursor = connection.cursor()

    #Query Canva 1
    #joy
    cursor.execute("""
         SELECT SUM(joy) FROM data_demo;
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Shocked
    cursor.execute("""
         SELECT SUM(Shocked) FROM data_demo;
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Neutral
    cursor.execute("""
         SELECT SUM(Neutral) FROM data_demo;
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Hate
    cursor.execute("""
         SELECT SUM(Hate) FROM data_demo;
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #sad
    cursor.execute("""
         SELECT SUM(sad) FROM data_demo;
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #angrt
    cursor.execute("""
         SELECT SUM(angrt) FROM data_demo;
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #amazed
    cursor.execute("""
         SELECT SUM(amazed) FROM data_demo;
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Query Canva 2-man
    #joy
    cursor.execute("""
         SELECT SUM(joy) FROM data_demo WHERE Sex = 'man';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Shocked
    cursor.execute("""
         SELECT SUM(Shocked) FROM data_demo WHERE Sex = 'man';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Neutral
    cursor.execute("""
         SELECT SUM(Neutral) FROM data_demo WHERE Sex = 'man';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Hate
    cursor.execute("""
         SELECT SUM(Hate) FROM data_demo WHERE Sex = 'man';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #sad
    cursor.execute("""
         SELECT SUM(sad) FROM data_demo WHERE Sex = 'man';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #angrt
    cursor.execute("""
         SELECT SUM(angrt) FROM data_demo WHERE Sex = 'man';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #amazed
    cursor.execute("""
         SELECT SUM(amazed) FROM data_demo WHERE Sex = 'man';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)


    #Query Canva 2-woman
    #joy
    cursor.execute("""
         SELECT SUM(joy) FROM data_demo WHERE Sex = 'woman';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Shocked
    cursor.execute("""
         SELECT SUM(Shocked) FROM data_demo WHERE Sex = 'woman';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Neutral
    cursor.execute("""
         SELECT SUM(Neutral) FROM data_demo WHERE Sex = 'woman';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Hate
    cursor.execute("""
         SELECT SUM(Hate) FROM data_demo WHERE Sex = 'woman';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #sad
    cursor.execute("""
         SELECT SUM(sad) FROM data_demo WHERE Sex = 'woman';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #angrt
    cursor.execute("""
         SELECT SUM(angrt) FROM data_demo WHERE Sex = 'woman';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #amazed
    cursor.execute("""
         SELECT SUM(amazed) FROM data_demo WHERE Sex = 'woman';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Query Canva 3-pr
    #joy
    cursor.execute("""
         SELECT SUM(joy) FROM data_demo WHERE dp = 'PR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Shocked
    cursor.execute("""
         SELECT SUM(Shocked) FROM data_demo WHERE dp = 'PR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Neutral
    cursor.execute("""
         SELECT SUM(Neutral) FROM data_demo WHERE dp = 'PR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Hate
    cursor.execute("""
         SELECT SUM(Hate) FROM data_demo WHERE dp = 'PR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #sad
    cursor.execute("""
         SELECT SUM(sad) FROM data_demo WHERE dp = 'PR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #angrt
    cursor.execute("""
         SELECT SUM(angrt) FROM data_demo WHERE dp = 'PR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #amazed
    cursor.execute("""
         SELECT SUM(amazed) FROM data_demo WHERE dp = 'PR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Query Canva 3-IT
    #joy
    cursor.execute("""
         SELECT SUM(joy) FROM data_demo WHERE dp = 'IT';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Shocked
    cursor.execute("""
         SELECT SUM(Shocked) FROM data_demo WHERE dp = 'IT';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Neutral
    cursor.execute("""
         SELECT SUM(Neutral) FROM data_demo WHERE dp = 'IT';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Hate
    cursor.execute("""
         SELECT SUM(Hate) FROM data_demo WHERE dp = 'IT';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #sad
    cursor.execute("""
         SELECT SUM(sad) FROM data_demo WHERE dp = 'IT';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #angrt
    cursor.execute("""
         SELECT SUM(angrt) FROM data_demo WHERE dp = 'IT';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #amazed
    cursor.execute("""
         SELECT SUM(amazed) FROM data_demo WHERE dp = 'IT';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)


    #Query Canva 3-HR
    #joy
    cursor.execute("""
         SELECT SUM(joy) FROM data_demo WHERE dp = 'HR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Shocked
    cursor.execute("""
         SELECT SUM(Shocked) FROM data_demo WHERE dp = 'HR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Neutral
    cursor.execute("""
         SELECT SUM(Neutral) FROM data_demo WHERE dp = 'HR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #Hate
    cursor.execute("""
         SELECT SUM(Hate) FROM data_demo WHERE dp = 'HR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #sad
    cursor.execute("""
         SELECT SUM(sad) FROM data_demo WHERE dp = 'HR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #angrt
    cursor.execute("""
         SELECT SUM(angrt) FROM data_demo WHERE dp = 'HR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    #amazed
    cursor.execute("""
         SELECT SUM(amazed) FROM data_demo WHERE dp = 'HR';
    """)
    data = cursor.fetchone()[0]
    arr.append(data)

    return arr


def test_api1(request):

    #先撈POST request body，輸入應該會是一個dict
    body = request.POST

    #將body內的name取出
    name = body['name']
    
    #建立新的DBTest object
    new_obj = DBTest()

    #把新建立的object內的test屬性改成"I love {POST['name']}"
    new_obj.test = "I love " + name

    #儲存object
    new_obj.save()

    #回傳200，這裡使用JsonResponse，data回傳格式為dict，將name與成功訊息結合方便察看結果
    return JsonResponse(data={'msg':name + ' add object success.'}, status=200)