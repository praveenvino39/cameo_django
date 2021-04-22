from django.urls import path
from cameo import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', view=views.homepage, name='homepage'),
    path('cameo/<str:username>', view=views.show_cameo, name='show_cameo'),
    path('login/user', view=views.login_view, name="login_page"),
    path('login', view=views.login_user, name='login'),
    path('logout', view=views.logout_user, name='logout'),
]
