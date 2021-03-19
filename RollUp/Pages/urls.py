from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home1'),
    path('login/', LoginPageView.as_view(), name = 'login'),
    path('login/newaccount', LoginNewAccount.as_view(), name = 'loginnewaccount'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('classinfo/',ClassInfoPageView.as_view(),name = 'classinfo'),
    path('account/',AccountPage.as_view(),name = 'account'),
    path('account/schedule',SchedulePage.as_view(), name = 'schedule'),
    path('account/schedule/signup',SignupClassPage.as_view(), name = 'signup'),
    path('account/covidreport',CovidReportPage.as_view(), name = 'covidreport'),
    path('account/contact',ContactPage.as_view(), name = 'contact'),
    path('account/FAQ',FAQPage.as_view(),name ='FAQ')
]