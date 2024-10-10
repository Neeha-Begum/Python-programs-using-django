from django.shortcuts import render

# Create your views here.
def func1(request):
    result=None
    if request.method=='POST':
        a=int(request.POST.get('num'))
        #print(a)
        if a%2==0:
            result=True
        else:
            result=False
    return render(request,'index.html',{'res':result})


def func2(request):
    count=0
    if(request.POST.get('snum') is not None):
        a=int(request.POST.get('snum'))
    else:
        a=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    res=count==2
    return render(request,'prime.html',{'result':res})


def func3(request):
    result=None
    if request.method=='POST':
            a=int(request.POST.get('num2'))
            b=int(request.POST.get('num3'))
            if a > b:
                result=True
            else:
                result=False
    return render(request,'greatest.html',{'res':result})

def func4(request):
    result=None
    if request.method=='POST':
        a=int(request.POST.get('arm'))
        size=len(str(a))
        temp=a
        sum=0
        if(a>0):
            while a>0:
                m=a%10
                sum=sum+(m**size)
                a=a//10
            if sum==temp:
                result=True
            else:
                result=False
    return render(request,'armstrong.html',{'armstrong':result})

def func5(request):
    a=None
    s='No response yet'
    if request.method=='POST':
         a=str(request.POST.get('sname'))
         s=  'Hi ' +  a
    return render(request,'hi.html',{'res':s})


