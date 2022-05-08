from django.urls import path
from .views import *

urlpatterns=[
    path('Librarianregister',LibrarianRegistration.as_view(),name="registration"),
    path('LibrarianLogin',LibrarianLogin.as_view(),name="login"),
    path('MemberRegister',MemberRegistration.as_view()),
    path('MemberLogin',MemberLogin.as_view())
]