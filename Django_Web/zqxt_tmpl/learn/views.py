from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #string = u"我在自强学堂学习Django，用它来建网站"
    #return render(request,'home.html',{'string':string})
    #TutorialList = ["Html","CSS","jQuery","Python","Django"]
    #return render(request,'home.html',{'TutorialList':TutorialList})
    #info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
   # return render(request, 'home.html', {'info_dict': info_dict})
   # List = map(str, range(100))# 一个长度为100的 List
   # return render(request, 'home.html', {'List': List})
    pass

def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
