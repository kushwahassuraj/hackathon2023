from django.http import HttpResponse
from django.shortcuts import render,redirect

# from .form import user
# from .quiz import fun_quiz
# from service.models import service
from feeds.models import feed_fun
# from lol import settings
import os
def info(r):

    return render(r,'info.html')
def local(r):

    return render(r,'local.html')
def index(r):
    data_obj=feed_fun.objects.all().order_by('location')#this create a object of all file and sorted by title fied
    if r.method=="GET":
        st=r.GET.get('search')
        if st!=None:
            data_obj=feed_fun.objects.filter(location__icontains=st)
    data={
        'data':data_obj
    }
    return render(r,'index.html',data)
# 
# def aboutus(r,id):
#     return HttpResponse(id)

def indexx(r,id):
    data_obj=feed_fun.objects.all().order_by('location')#this create a object of all file and sorted by title fied
    if r.method=="GET":
        st=r.GET.get('search')
        if st!=None:
            data_obj=feed_fun.objects.filter(location__icontains=st)
            
           
        else:
            data_obj=feed_fun.objects.filter(location__icontains=id)
            
    data={
        'data':data_obj
    }
    return render(r,'index.html',data)

import os
import openpyxl
import pandas as pd
from django.conf import settings


def mc(request,id):
    # Get the file path for the xlsx file
    file_path = os.path.join(settings.BASE_DIR, 'static', f'{id}.xlsx')

    # Open the xlsx file
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    
    data = []
    for row in ws.iter_rows(values_only=True):
        data.append(row)

    df = pd.DataFrame(data[1:], columns=data[0])
    table = df.to_html()

    return render(request, 'mcd.html', {'data': table,'title':id})
def text(r):
   
  
    try:
        if r.method=="POST":
            name=r.POST.get('name')
            location=r.POST.get('location')
            message=r.POST.get('message')
            en=feed_fun(name=name,location=location,message=message)
            en.save()
            return render(r,'text.html',{'ad':"thanks for contacing us",'ty':"text"}) 
           
    except:
        pass

    return render(r,'text.html',{'ad':"send message",'ty':"submit"})
    #this statment will change the contents of submit button after clicking in it
    return redirect("/") #this will redirect to about page.
# def index(r):
#     table_data=service.objects.all()
#     static_dir = os.path.join(settings.BASE_DIR, 'static/images') # replace 'static' with the name of your static directory
#     files = [f for f in os.listdir(static_dir) if os.path.isfile(os.path.join(static_dir, f))]
    

#     data={
#         'title':'Home page',
#         'list':['python','c++','java'],
#         'dic':[
#         {'name':'rav','phone':'4554'},
#         {'name':'anuj','phone':'7854'},
#         ],
#         'tdata':table_data,
#         'range':files
#     }
  
#     return render(r,'index.html',data)
# # def calculator(r):
# #     c=0
# #     cl=user()
# #     data={
# #         'form':cl
# #     }
# #     return render(r,'calculator.html',data)
# def calculator(request):
#     try:
#         if request.method == 'POST':
#             form = user(request.POST)
#             if form.is_valid():
#                 n1 = form.cleaned_data['n1']
#                 o=form.cleaned_data['opt']
#                 n2 = form.cleaned_data['n2']
            
#                 d=n1+str(o)+n2
#                 total=eval(d)
            
#                 return render(request, 'calculator.html', {'total': total,'title':'Output'})
#         else:
#             form = user()
#     except:
#         pass
#     return render(request, 'calculator.html', {'form': form,'total':'calculate','title':'Calculator'})

# def quiz(request):
#     try:
#         m=fun_quiz().out[0]
        
#         if request.method == 'POST':
#             form = fun_quiz(request.POST)
#             if form.is_valid() :
#                 o=request.POST['opt']

            
                
#                 if o ==fun_quiz().out[1]:
#                     return render(request, 'quiz.html', {'total': 'correct','title':'your ans is','q':''})
                   

#                 else:
#                     return render(request, 'quiz.html', {'total':'wrong' ,'title':'your ans is','q':''})
           
                    
#         else:
            
#             form = fun_quiz()
            
#     except:
#        pass
#     return render(request, 'quiz.html', {'form': form,'total':'submit','title':'Quiz','q':m})
