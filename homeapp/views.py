from django.shortcuts import render

def homeview(request):
    return render(request,'homeindex.html')
