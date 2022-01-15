from django.urls import path
from cameo import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', view=views.homepage, name='homepage'),
    # path('cameo/<str:username>', view=views.show_cameo, name='show_cameo'),
    path('', view=views.homepage_api, name="homepage_api"),
    path('category/<str:category>', view=views.filter_by_category_api, name='category_api'),
    path('login/', view=views.login_api, name="login_page_api"),
]
