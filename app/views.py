from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#returning string by using FBV

from django.views.generic import View,TemplateView
from app.forms import *

def FBV(request):
    return HttpResponse('<h1>This is Function Based View</h1>')


#returning string by using CBV

class CBV(View):
    def get(self,request):
        return HttpResponse('<h1>This is CBV</h1>')


#returning A HTML page by using FBV

def FBV_template(request):
    return render(request,'FBV_template.html')

#returning A HTML page by using CBV

class CBV_template(View):
    def get(self,request):
        return render(request,'CBV_template.html')



# validating Form by using FBV

def FBV_form(request):
    form=Student()
    if request.method=="POST":
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'FBV_form.html',context={'form':form})


# Validating Form By using CBV

class CBV_form(View):
    def get(self,request):
        form=Student()
        return render(request,'CBV_form.html',context={'form':form})

    def post(self,request):
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

# Dont use View Class whenever u r dealing with Templates and Forms

class CBV_TemplateView(TemplateView):
    template_name='CBV_template.html'


























