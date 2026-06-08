from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    admin_login,
    admin_dashboard,
)

urlpatterns = [

    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'login/',
        user_login,
        name='login'
    ),

    path(
        'logout/',
        user_logout,
        name='logout'
    ),
     path(
     'admin-login/',
     admin_login,
     name='admin_login'),
     
     path(
     'admin-dashboard/',
     admin_dashboard,
     name='admin_dashboard'
),
]