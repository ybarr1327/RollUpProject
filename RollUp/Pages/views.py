from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from Pages.forms import CustomUserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from .models import Classes, Participants



# Create your views here.


def HomePageView(request):
    return render(request, "homepage/home.html")

def AboutPageView(request):
    return render(request,"about/aboutpage.html")

def ClassInfoPageView(request):
    return render(request, "classinfopage/classinfopage.html")

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('accountDash')

    else:
        f = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': f})

@login_required
def AccountDashPage(request):
    return render(request, "accountDashPage/accountDashPage.html")
@login_required
def SchedulePage(request):
    all_classes = Classes.objects.order_by('date')
    contextOfClasses = {
        'classes' : all_classes
    }

    if request.method == 'POST' and 'SignUpForClass' in request.POST:
        user = request.user
        #get the user data

        
        #get the clicked checkboxes
        check_boxes = request.POST.getlist('checkbox')
        # print(check_boxes)
        for i in check_boxes:
            newParticipant = Participants()
            newParticipant.email = user.email
            newParticipant.name = user.first_name +" "+ user.last_name
            newParticipant.class_id = Classes.objects.get(id = i)
            newParticipant.save()
        
        
        
            
        
        # return user to required page
        return redirect('/accountDash/schedule/signup/') 

    return render(request, "accountDashPage/schedulePage.html", contextOfClasses)

@login_required
def SignupClassPage(request):
    return render(request, "accountDashPage/signupclassPage.html")

@login_required
def CovidReportPage(request):
    return render(request, "accountDashPage/covidreportPage.html") 

def ContactPage(request):
    return render(request, "accountDashPage/contactPage.html")
@login_required
def FAQPage(request):
    return render(request, "accountDashPage/FAQPage.html")
