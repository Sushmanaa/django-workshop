from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def homepage(request):
    return render(request,"wcount/home.html")
def about(request):
    return render(request,"wcount/about.html")
def count(request):
    return render(request,"wcount/count.html")
def count(request):
        fulltext=request.GET['text']
        word_count=len(fulltext.split())
        word_dict={}
        for w in fulltext.split():
                if w in word_dict:
                        word_dict[w]+=1
                else:
                        word_dict[w]=1
        l = list(word_dict.items())
        return render(request,"wcount/count.html",{'fulltext':fulltext ,'word_count':word_count,'word_dict':word_dict,"l":l})