from django.shortcuts import HttpResponse,render,redirect
from db.models import Student



def Home (request):

    # data={"Student":Student.objects.all() 
    students= Student.objects.all()
    data={"data":students}
    
    if request.method == 'POST':
        name= request.POST.get('name')
        age= request.POST.get('age')
        city= request.POST.get('city')
        image= request.FILES.get('image')

        Student(name=name,age=age,city=city,image=image).save()
       
        return redirect('/')
    

    # else:
    #     return redirect("/")
    return render(request,"home.html",data)

def About(request):
    return render(request,"about.html")

def Contact (request):
    return render (request,"contact.html")

def Help (request):
    return render(request,"help.html")
