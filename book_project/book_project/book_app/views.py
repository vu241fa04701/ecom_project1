from django.http import HttpResponse
from django.shortcuts import render
from .models import UserModel
# Create your views here.
def home_page(request):
    return render(request,"home.html",{"names":
                                       [{"name":"Prathyu"},
                                        {"name":"Susmitha"},
                                        {"name":"Poojitha"},
                                        {"name":"Thanmai"}

    ],})
def contact(request):
    return render(request,"contact.html",{"range":range(1,10)})
def profile(request):
    return render(request,"profile.html",{"name":"Amit","email":"amit123@gmail.com","role":"admin","user_data":[
        {"name":"Amit","email":"abc@gmail.com"},
        {"name": "Jon", "email": "defgh@gmail.com"},
        {"name": "Alex", "email": "ijklm@gmail.com"}
    ]})
def grades(request,marks):
    return render(request,"grade.html",context={"marks":marks})
def add_user(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        data=UserModel.objects.create(
            name=name,
            email=email
        )
        return HttpResponse("User added")


    return render(request,"user_form.html")