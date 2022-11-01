from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.slogin),
    #path('logout/', views.slogout),

]