from django.shortcuts import render

# Create your views here.
def States(request):
    return render(request,'States.html')
def Andhra_Pradesh(request):
    return render(request,'Andhra_Pradesh.html')
def Telangana(request):
    return render(request,'Telangana.html')
def TamilNadu(request):
    return render(request,"TamilNadu.html")
def Karnataka(request):
    return render(request,"Karnataka.html")
def Kerala(request):
    return render(request,'Kerala.html')
def Maharastra(request):
    return render(request,'Maharastra.html')
def Orissa(request):
    return render(request,'Orissa.html')