from django.urls import path
from .views import Signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', Signup.as_view(), name = "signup"),
    path('login/', LoginView.as_view(template_name="accounts/login.html", next_page="home"), name="login"),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
]