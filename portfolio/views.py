from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm


def home(request):

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            # form.save()
            return redirect('upload')

    else:
        form = ContactForm()

    return render(request, 'portfolio/home.html', {'form': form})



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


# view for project case study
def food_project(request):
    return render(request, 'portfolio/food_project.html')

def book_review(request):
    return render(request, 'portfolio/book_review.html')

def cake_customize(request):
    return render(request, 'portfolio/cake_customize.html')