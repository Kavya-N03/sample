from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.registerUser,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('pics/',views.pics,name="pics"),
]
