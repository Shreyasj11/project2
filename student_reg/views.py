from django.shortcuts import render
from django.http import HttpResponse
from student_reg.models import student_details
from  student_reg import forms

# Create your views here.
def home(request):
    return render(request,'std_myapp/home.html')
   # return HttpResponse("welcome to Students Registration")

def reg(Request):
    s_reg=forms.std_form
    return render(Request, 'std_myapp/reg.html',context=dict({'form_d':s_reg}))
    #return HttpResponse(" Students Registration page")

def report(Request):
    #return HttpResponse("student reports")
    temp_std_details=student_details.objects.order_by('std_id')
    std_det_dict={'insert_std_det':temp_std_details}
    return render(Request,'std_myapp/report.html',context=std_det_dict)

