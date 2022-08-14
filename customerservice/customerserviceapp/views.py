from django import forms
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _

from customerserviceapp.forms import TicketFormCreate, TicketFormEditAdmin, TicketFormEditDist
from customerserviceapp.models import Ticket
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def home(request):
    return redirect(show_tickets)

@login_required(login_url='/sign-in/')
@user_passes_test(lambda u:u.is_superuser or u.is_receiver, login_url='/')
def create_ticket(request):
    ticket_form = TicketFormCreate()
    if request.method == "POST":
        ticket_form = TicketFormCreate(request.POST)
        if ticket_form.is_valid():
            owner = request.user
            new_ticket = ticket_form.save(commit=False)
            new_ticket.owner = owner
            new_ticket.status = Ticket.PACKING
            new_ticket.save()

            return redirect(show_tickets)
    return render(request, 'create_ticket.html', {'ticket_form': ticket_form})

@login_required(login_url='/sign-in/')
def show_tickets(request):
    if request.user.is_superuser:
        ticket = Ticket.objects.order_by("-id").values()
        return render(request, 'ticket_admin.html', {"tickets": list(ticket)})

    ticket = Ticket.objects.order_by("-id")[:10]
    return render(request, 'ticket.html', {"tickets": ticket})

@login_required(login_url='/sign-in/')
@user_passes_test(lambda u:u.is_superuser or u.is_distributor, login_url='/')
def edit_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        if request.user.is_superuser:
            form = TicketFormEditAdmin(request.POST, request.FILES, instance=ticket)
        else:
            form = TicketFormEditDist(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect(show_tickets)
    else:
        if request.user.is_superuser:
            form = TicketFormEditAdmin(instance=ticket)
        else:
            form = TicketFormEditDist(instance=ticket)

    return render(request, 'edit_ticket.html', {"form": form})

@login_required(login_url='/sign-in/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(change_password)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

@login_required(login_url='/sign-in/')
@user_passes_test(lambda u:u.is_superuser, login_url='/')
def management_home(request):
    return render(request, 'management/base_management.html')

@login_required(login_url='/sign-in/')
@user_passes_test(lambda u:u.is_superuser, login_url='/')
def management_report(request):
    return render(request, 'management/report.html')