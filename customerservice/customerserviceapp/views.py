from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from customerserviceapp.forms import UserForm, TicketForm, CommentForm
from customerserviceapp.models import Ticket, Comment
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def home(request):
    return redirect(show_tickets)

def sign_up(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(create_ticket)
    return render(request, 'sign_up.html', {'user_form': user_form})

@login_required(login_url='/sign-in/')
def create_ticket(request):
    ticket_form = TicketForm()
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            owner = request.user
            new_ticket = ticket_form.save(commit=False)
            new_ticket.owner = owner
            new_ticket.status = Ticket.INBACKLOG
            new_ticket.save()

            return redirect(show_tickets)
    return render(request, 'create_ticket.html', {'ticket_form': ticket_form})

@login_required(login_url='/sign-in/')
def show_tickets(request):
    ticket = Ticket.objects.order_by("-id")
    return render(request, 'ticket.html', {"tickets": ticket})

@login_required(login_url='/sign-in/')
def add_comment(request, ticket_id):
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user = request.user
            new_comment = comment_form.save(commit=False)
            new_comment.user = user
            new_comment.ticket = Ticket.objects.get(id=ticket_id)
            new_comment.save()

            return redirect(ticket_details, ticket_id)
    return render(request, 'add_comment.html', {'comment_form': comment_form})

@login_required(login_url='/sign-in/')
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    comments = Comment.objects.filter(ticket=ticket)
    return render(request, 'ticket_details.html', {'ticket': ticket, 'comments': comments})

@login_required(login_url='/sign-in/')
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    ticket = comment.ticket
    if request.user != comment.user:
        Comment.objects.filter(id=comment_id).delete()
    else:
        messages.error(request, "Only the owner of this comment can delete it")
    #return redirect(ticket_details, ticket.id)
