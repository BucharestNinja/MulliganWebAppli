from django.shortcuts import render
import random
import numpy
from django.http.response import HttpResponse


# Create your views here.
class mulliganHand:

 def post_list(request):
     c={
        "messege":"sumple messege",
        }
     return render(request, 'mulligan/post_list.html', c)

 def getDeckList(request):

      d={
        "firstHand":request.POST["saveDeck"],
        }
      loop=1
      deck=[]
      data =d["firstHand"]#デッキのデータを読み込む
      for cardList in data.splitlines():
        num,*card=cardList.split(" ",1)#カードの枚数とカードの名前を分ける
        stripNum=int(num.rstrip())
        #print(stripNum)
        while loop<=stripNum:
             deck.extend([*card]) #デッキリストのカードを先頭から一行ずつ読み込む
             loop+=1
        loop=1

      a={"deck":deck[]}
      #print(i)

      return render(request,"mulligan/getDeckList.html",a)
