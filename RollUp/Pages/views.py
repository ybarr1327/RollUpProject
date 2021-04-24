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
    all_classes = Classes.objects.order_by('date') #get all the entries from the classes table ordered by date
    #store the context of the classes to pass to the render
    contextOfClasses = {  
        'classes' : all_classes
    }

    #if the user pressed the sign up button
    if request.method == 'POST' and 'SignUpForClass' in request.POST:
        
        
        #get the clicked checkboxes, this gets a list of numbers that contain the checkbox id's, 
        # these ids are set to the value of the class id they are representing
        check_boxes = request.POST.getlist('checkbox')
        if check_boxes: #if there were objects checked
            user = request.user # get the user data
            
            # the following are lists to store which classes were able to be signed up for or not
            sucessfulClassSignups = []
            failedClassSignups = []
            
            # print(check_boxes)
            
            #for all the class ids / checkboxes selected
            for i in check_boxes:
                #get the class object associated with that class id
                classToSignUpFor = Classes.objects.get(id=i)
                
                # if there is room in that class, sign up
                if classToSignUpFor.num_signed_up < classToSignUpFor.size:
                    
                    #add this class id to the sucessful signup list
                    sucessfulClassSignups.append(classToSignUpFor.id)
                    
                    #create a new participant and store it
                    newParticipant = Participants()
                    newParticipant.email = user.email
                    newParticipant.name = user.first_name +" "+ user.last_name
                    newParticipant.class_id = classToSignUpFor
                    newParticipant.save()
                else: # if the class is full, then add it to the fail list
                    failedClassSignups.append(classToSignUpFor.id)
            
            # print(sucessfulClassSignups)
            # print(failedClassSignups)

            #store the sucess and fail lists in a tuple
            signupconfimation = (sucessfulClassSignups,failedClassSignups)
            
            #store the signup confimation tuple in a session
            #NOTE: a session is like a hash table / dictionary that stores data on a string key wihtin the database
            #NOTE: this is mainly useful for passing in between different views / different urls 
            request.session['signupdata'] = signupconfimation

            

            # return user to required page which is the signup page
            return redirect('signup')



        
    # render the page with the html and the context of classes to show all the available classes
    return render(request, "accountDashPage/schedulePage.html", contextOfClasses)

@login_required
def SignupClassPage(request):
    classes_signed_up_for = request.session['signupdata'] # pull the signup data from the session database/table
    del request.session['signupdata'] #delete the key/item because it is no longer needed to be stored since we just stored it in a variable
    
    #the following code prints the session items currently stored
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))

    sucessfulSignups = [] #this is a list that will store the actual class objects of the classes that were sucessfull signed up for
    failedSignups = [] # this is a list that will store the actual class objects of the classes that were nor able to be signed up for

    for a in classes_signed_up_for[0]: # for all the sucessful ones, add their objects to the list
        sucessfulSignups.append(Classes.objects.get(id=a))
    for b in classes_signed_up_for[1]: # for all the failed ones, add their objescts to the list
        failedSignups.append(Classes.objects.get(id=b))


    #strore the two lists as the context dictionary
    context = { 
        'succeed' : sucessfulSignups,
        'failed' : failedSignups
    }
    #render the view with the context
    return render(request, "accountDashPage/signupclassPage.html", context)

@login_required
def CovidReportPage(request):
    return render(request, "accountDashPage/covidreportPage.html") 

def ContactPage(request):
    return render(request, "accountDashPage/contactPage.html")
@login_required
def FAQPage(request):
    return render(request, "accountDashPage/FAQPage.html")
