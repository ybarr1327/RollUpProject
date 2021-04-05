
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import path, include

from Pages.views import *

from django.urls import path
from django.urls import include as inc1

from django.conf.urls import url
from django.conf.urls import include as inc2


urlpatterns = [
    url (r"^accounts/",inc2("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    path('',HomePageView, name='home'),
    path('about/', AboutPageView, name = 'about'),
    path('classinfo/',ClassInfoPageView,name = 'classinfo'),
    path('accountDash/',AccountDashPage,name = 'accountDash'),
    path('accountDash/schedule/',SchedulePage, name = 'schedule'),
    path('accountDash/schedule/signup/',SignupClassPage, name = 'signup'),
    path('accountDash/covidreport/',CovidReportPage, name = 'covidreport'),
    path('contact/',ContactPage, name = 'contact'),
    path('accountDash/FAQ/',FAQPage,name ='FAQ'),
]