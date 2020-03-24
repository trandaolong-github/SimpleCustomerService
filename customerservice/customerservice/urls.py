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
from django.urls import path
from django.contrib.auth import views as auth_views
from customerserviceapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', auth_views.LoginView.as_view(template_name='sign_in.html'), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/'), name='sign-out'),
    path('create-ticket/', views.create_ticket, name='create-ticket'),
    path('show-tickets/', views.show_tickets, name='show-tickets'),
    path('ticket-details/<int:ticket_id>/', views.ticket_details, name='ticket-details'),
    path('add-comment/<int:ticket_id>/', views.add_comment, name='add-comment'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete-comment'),
]
