"""FirstPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  brpl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='dropdown'),
    path('get_divisions/', views.get_divisions, name='get_divisions'),
    path('get_subdivisions/',views.get_subdivisions ,name='get_subdivisions'),
    path('upload_form/',views.homepage_view,name='upload_form'),
    path('get_data/', views.get_data, name='get_data'),
    # path('test_3/', views.test_3_view, name='test_3'),
    path('test_3/', views.test_3_page, name='test_3_page'),

]
    
