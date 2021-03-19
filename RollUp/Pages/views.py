from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'homepage/home.html'

class LoginPageView(TemplateView):
    template_name = 'login/loginpage.html'

class LoginNewAccount(TemplateView):
    template_name = 'login/newAccountPage.html'

class AboutPageView(TemplateView):
    template_name = 'about/aboutpage.html'

class ClassInfoPageView(TemplateView):
    template_name = 'classinfopage/classinfopage.html'

class AccountPage(TemplateView):
    template_name = 'accountPage/accountPage.html'

class SchedulePage(TemplateView):
    template_name = 'accountPage/schedulePage.html'

class SignupClassPage(TemplateView):
    template_name = 'accountPage/signupclassPage.html'  

class CovidReportPage(TemplateView):
    template_name = 'accountPage/covidreportPage.html' 

class ContactPage(TemplateView):
    template_name = 'accountPage/contactPage.html'

class FAQPage(TemplateView):
    template_name = 'accountPage/FAQPage.html'
