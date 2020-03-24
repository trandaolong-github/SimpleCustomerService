from django import forms
from django.contrib.auth.models import User
from customerserviceapp.models import Ticket, Comment


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )