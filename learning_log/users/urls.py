"""为应用程序users定义URL模式"""


from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

# 修改模板路径
LoginView.template_name = 'users/login.html'

urlpatterns = [
    #登陆界面
    path('login/',LoginView.as_view(),name='login'),

    #注销
    path('logout/',views.logout_view,name='logout'),

    #注册页面
    path('register/',views.register,name='register'),
]

app_name = 'users'
