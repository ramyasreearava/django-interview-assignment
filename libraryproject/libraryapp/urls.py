from django.urls import path
from .views import *

urlpatterns=[
    path('LibrarianRegister',LibrarianRegistration.as_view(),name="registration"),
    path('LibrarianLogin',LibrarianLogin.as_view(),name="login"),
    path('MemberRegister',MemberRegistration.as_view()),
    path('MemberLogin',MemberLogin.as_view()),
    path('GetallMembers',Getallmembers.as_view()),
    path('UpdateMembers/<int:id>',UpdateMembers.as_view()),
    path('DeleteMembers/<int:id>',DeleteMembers.as_view())
]