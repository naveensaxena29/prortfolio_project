from django.shortcuts import render,redirect
from .models import Contact

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')



# from django.shortcuts import render, redirect
# from .models import Contact

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(name)   # DEBUG

        if name and email and message:

            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            return redirect("/")

    return render(request, "portfolio/contact.html")