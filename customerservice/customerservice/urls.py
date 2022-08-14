"""customerservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from customerserviceapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sign-in/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/'), name='sign-out'),
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('show-tickets/', views.show_tickets, name='show-tickets'),
    path('edit-ticket/<int:ticket_id>/', views.edit_ticket, name='edit-ticket'),
    path('change-password/', views.change_password, name='change-password'),
    path('management/', views.management_home, name='management-home'),
    path('management/report/', views.management_report, name='management-report'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
