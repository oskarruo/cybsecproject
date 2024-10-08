"""
URL configuration for calendar_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from pages.views import home_view, register_view, add_event_view, delete_event_view, search_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('register/', register_view),
    path('add_event/', add_event_view),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete_event/<int:event_id>/', delete_event_view),
    path('search/', search_view)
]
