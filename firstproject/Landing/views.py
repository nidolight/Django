from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'Landing/index.html')
    # return HttpResponse("hello")


def study(req):
    return render(req,"Landing/study.html")

def css_example(req):
    return render(req,"Landing/css_example.html")

def index2(request):
    return render(request,'Landing/index2.html')

