from django.urls import path
from . import views
urlpatterns= [
    path("signup/",views.piyushlmsSignupUser.as_view()),
    path("getAllUser/",views.piyushlmsGetUserDetails.as_view()),
    path("updateEmail/", views.piyushlmsUpdateEmail.as_view()),
    path("deleteUser/<number>/", views.piyushlmsDeleteUser.as_view()),
]