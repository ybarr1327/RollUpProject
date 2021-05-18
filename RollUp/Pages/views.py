from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from Pages.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Classes, Participants
from datetime import date, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.utils.dateparse import parse_date
from django.db.models import F


# Create your views here.


def HomePageView(request):
    return render(request, "homepage/home.html")


def AboutPageView(request):
    return render(request, "about/aboutpage.html")


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
    today = date.today()

    # get all the entries from the classes table ordered by date
    all_classes = Classes.objects.order_by('date').filter(
        date__range=[today, today + timedelta(days=30)])
    # store the context of the classes to pass to the render
    contextOfClasses = {
        'classes': all_classes
    }

    # if the user pressed the sign up button
    if request.method == 'POST' and 'SignUpForClass' in request.POST:

        # get the clicked checkboxes, this gets a list of numbers that contain the checkbox id's,
        # these ids are set to the value of the class id they are representing
        check_boxes = request.POST.getlist('checkbox')
        if check_boxes:  # if there were objects checked
            user = request.user  # get the user data

            # the following are lists to store which classes were able to be signed up for or not
            sucessfulClassSignups = []
            failedClassSignups = []
            alreadySignedUpFail = []

            # print(check_boxes)

            # for all the class ids / checkboxes selected
            for i in check_boxes:
                # get the class object associated with that class id
                classToSignUpFor = Classes.objects.get(id=i)

                if Participants.objects.filter(class_id=i, username=user.username).exists() == False:
                    # if there is room in that class, sign up
                    if classToSignUpFor.num_signed_up < classToSignUpFor.size:

                        # add this class id to the sucessful signup list
                        sucessfulClassSignups.append(classToSignUpFor.id)
                        
                        #this increases the num_signed_up value
                        classToSignUpFor.num_signed_up = F('num_signed_up') + 1
                        classToSignUpFor.save()
                        # create a new participant and store it
                        newParticipant = Participants()
                        newParticipant.email = user.email
                        newParticipant.name = user.first_name + " " + user.last_name
                        newParticipant.class_id = classToSignUpFor
                        newParticipant.username = str(user.username)
                        newParticipant.save()
                    else:  # if the class is full, then add it to the fail list
                        failedClassSignups.append(classToSignUpFor.id)
                else:
                    alreadySignedUpFail.append(classToSignUpFor.id)

            # print(sucessfulClassSignups)
            # print(failedClassSignups)

            # store the sucess and fail lists in a tuple
            signupconfimation = (sucessfulClassSignups,
                                 failedClassSignups, alreadySignedUpFail)

            if sucessfulClassSignups:
                email_msg = 'You signed up for the following classes:'

                for i in sucessfulClassSignups:
                    class_signed_up = Classes.objects.get(id=i)
                    email_msg += '\n' + class_signed_up.type + ' ' + \
                        str(class_signed_up.time) + ' ' + \
                            str(class_signed_up.date)
                send_mail('Roll Up Project - Sign Up Successful',
                          email_msg,
                          'rollupproject@gmail.com',
                                [user.email]
                          )

            # store the signup confimation tuple in a session
            # NOTE: a session is like a hash table / dictionary that stores data on a string key wihtin the database
            # NOTE: this is mainly useful for passing in between different views / different urls
            request.session['signupdata'] = signupconfimation

            # store the signup confimation tuple in a session
            # NOTE: a session is like a hash table / dictionary that stores data on a string key wihtin the database
            # NOTE: this is mainly useful for passing in between different views / different urls
            request.session['signupdata'] = signupconfimation

            # return user to required page which is the signup page
            return redirect('signup')

    # render the page with the html and the context of classes to show all the available classes
    return render(request, "accountDashPage/schedulePage.html", contextOfClasses)


@login_required
def SignupClassPage(request):
    # pull the signup data from the session database/table
    classes_signed_up_for = request.session['signupdata']
    # delete the key/item because it is no longer needed to be stored since we just stored it in a variable
    del request.session['signupdata']

    # the following code prints the session items currently stored
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))

    # this is a list that will store the actual class objects of the classes that were sucessfull signed up for
    sucessfulSignups = []
    failedSignups = []  # this is a list that will store the actual class objects of the classes that were nor able to be signed up for
    alreadySignedUp = []

    # for all the sucessful ones, add their objects to the list
    for a in classes_signed_up_for[0]:
        sucessfulSignups.append(Classes.objects.get(id=a))
    # for all the failed ones, add their objescts to the list
    for b in classes_signed_up_for[1]:
        failedSignups.append(Classes.objects.get(id=b))
    for c in classes_signed_up_for[2]:
        alreadySignedUp.append(Classes.objects.get(id=c))

    # strore the two lists as the context dictionary
    context = {
        'succeed': sucessfulSignups,
        'failed': failedSignups,
        'signedUpAlready': alreadySignedUp
    }
    # render the view with the context
    return render(request, "accountDashPage/signupclassPage.html", context)


@login_required
def MyClassesPage(request):
    # get the participant entries for every class the user is signed up for
    user = request.user
    Participants_Entries = Participants.objects.filter(username=user.username)

    # get the id's of each class
    SignUps = []
    for i in Participants_Entries:
        SignUps.append(i.class_id.id)

    # get the acutual classes based on the ids
    MyClasses = []
    for i in SignUps:
        MyClasses.append(Classes.objects.get(id=i))

    # define the context of MyClassesPage
    contextforMyclasses = {
        'classes': MyClasses
    }

    if request.method == 'POST' and 'UnregisterForClass' in request.POST:

        # get the clicked checkboxes, this gets a list of numbers that contain the checkbox id's,
        # these ids are set to the value of the class id they are representing
        check_boxes = request.POST.getlist('checkbox')
        if check_boxes:  # if there were objects checked
            # for all the class ids / checkboxes selected

            email_msg = 'You unregistered for the following classes:'

            for i in check_boxes:
                registrationToDelete = Participants.objects.get(class_id=i, username=user.username)
                
                #the following two lines removes from the num signed up variable
                if (registrationToDelete.class_id.num_signed_up - 1 >= 0):
                    registrationToDelete.class_id.num_signed_up = F('num_signed_up') - 1
                    registrationToDelete.class_id.save()
                

                email_msg += '\n' + registrationToDelete.class_id.type + ' ' + str(registrationToDelete.class_id.time) + ' ' + str(registrationToDelete.class_id.date)
                # get the participant entry associated with that class id and username
                
                registrationToDelete.delete()

            send_mail('Roll Up Project - Classes Successfully Unregistered', email_msg, 'rollupproject@gmail.com', [user.email])
            return redirect('MyClasses')

    return render(request, "accountDashPage/myClasses.html", contextforMyclasses)


@ login_required
def CovidReportPage(request):
    if request.method == "POST":
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        option = request.POST.get('chk')
        date = request.POST.get('date')
        AdditionalComments = request.POST.get('subject')


        # print(name)
        # print(email)
        # print(option)
        # print(date)
        # print(AdditionalComments) 

        if name and email and option and date:
            topic = 'COVID REPORT Sender Name: ' + name + ' Sender Email: ' + email
            body = "Type: " + option + "\nDate: " + date + "\nAdditional Comments: " + AdditionalComments
            send_mail(topic, body, email, ['rollupproject@gmail.com'])


    return render(request, "accountDashPage/covidreportPage.html")


def ContactPage(request):
    if request.method == 'POST' and 'Submit' in request.POST:
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        topic = request.POST.get('type')
        body = request.POST.get('subject')
       
        if name and email and topic != 'select' and body:
            topic += ' Sender Name: ' + name + 'Sender Email: ' + email

            send_mail(topic,body,email,['rollupproject@gmail.com'])
        

    return render(request, "accountDashPage/contactPage.html")


@ login_required
def FAQPage(request):
    return render(request, "accountDashPage/FAQPage.html")

def NotifyPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        dateStr = request.POST.get('date')
        temp_date = parse_date(dateStr)
        if(email and dateStr):
            listOfParticipantEntries = list(Participants.objects.filter(email = email).values("class_id"))
            filteredClassids = []
            emailList = []
            tempList = []
            uniqueEmail = []
            for i in listOfParticipantEntries:
                filteredClassids.append(i['class_id'])
            for x in filteredClassids:
                tempList= Participants.objects.filter(class_id = x).values('email')
                if tempList:
                    for y in tempList:
                        emailList.append(y['email'])
            uniqueEmail = list(set(emailList))

            if uniqueEmail:
                topic = "ROLLUPPROJECT- EMAIL REQUIRES YOUR ATTENTION"
                body = 'Dear Patron,\n You are recieving this email because it has been brought to our attention that there has been a COVID Exposure incident at our facility. We are therefore informing you that you attended a class that may have exposed you to the virus. We will continue to keep you informed as we learn more about the incident.\n Thank you for your time and feel free to contact us with any questions. \n Respectfully, \n RollUpProject'
                fromEmail = 'rollupproject@gmail.com'
                send_mail(topic, body, fromEmail, uniqueEmail)
            
            
            


    return render(request, 'notify/notify.html') 
