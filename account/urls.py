from django.urls import path
from account import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('changepassword/', views.changepassword, name="changepassword"),
]