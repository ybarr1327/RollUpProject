from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from Pages.forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required

# Create your views here.


def HomePageView(request):
    return render(request, "homepage/home.html")

def AboutPageView(request):
    return render(request,"about/aboutpage.html")

def ClassInfoPageView(request):
    return render(request, "classinfopage/classinfopage.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form":CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse("accountDash"))

@login_required
def AccountDashPage(request):
    return render(request, "accountDashPage/accountDashPage.html")
@login_required
def SchedulePage(request):
    return render(request, "accountDashPage/schedulePage.html")
@login_required
def SignupClassPage(request):
    return render(request, "accountDashPage/signupclassPage.html")  
@login_required
def CovidReportPage(request):
    return render(request, "accountDashPage/covidreportPage.html") 
@login_required
def ContactPage(request):
    return render(request, "accountDashPage/contactPage.html")
@login_required
def FAQPage(request):
    return render(request, "accountDashPage/FAQPage.html")
