from django.shortcuts import render

# Create your views here.
def func1(request):
    d={'results':[{'rollno':466,'name':'Alice','cgpa':8,'passed_subjects':57,'failed_subjects':0},
            {'rollno':488,'name':'John','cgpa':7,'passed_subjects':56,'failed_subjects':1},
            {'rollno':486,'name':'kate','cgpa':8,'passed_subjects':57,'failed_subjects':0},
            {'rollno':490,'name':'Tom','cgpa':6,'passed_subjects':52,'failed_subjects':5},
            {'rollno':498,'name':'Sam','cgpa':7,'passed_subjects':55,'failed_subjects':2}]}
    result=None
    if request.method=='POST':
        for record in d.get('results'):
            a=int(request.POST.get('num'))
            if a==record['rollno']:
                result=record
                break
    if result is not None:
        return render(request,'rollno.html',{'r':result})
    else:
        return render(request,'rollno.html')