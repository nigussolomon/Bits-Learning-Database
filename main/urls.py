from django.urls import path
from django.urls.conf import include
from .  import views as main_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main_views.home, name = 'homemain'),
    path('blog/', main_views.blog, name= 'blogmain'),
    path('register/', main_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'main/logout.html'), name="logout"),
    path('BLD/', include('database.urls'))
]
