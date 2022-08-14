from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from customerserviceapp.models import Ticket


class TicketFormEditDist(forms.ModelForm):
    customer = forms.CharField(disabled= True, required= False, label = "Khách hàng")
    quantity1 = forms.FloatField(disabled= True, required= False, label = "Đá loại 1 (Tấn)")
    quantity2 = forms.FloatField(disabled= True, required= False, label = "Đá loại 2 (Tấn)")
    quantity3 = forms.FloatField(disabled= True, required= False, label = "Đá loại 3 (Tấn)")
    quantity4 = forms.FloatField(disabled= True, required= False, label = "Đá loại 4 (Tấn)")
    class Meta:
        model = Ticket
        fields = ('customer', 'quantity1', 'quantity2', 'quantity3', 'quantity4', 'status')
        labels = {
            'status': 'Tình trạng'
        }


class TicketFormEditAdmin(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('customer', 'quantity1', 'quantity2', 'quantity3', 'quantity4', 'status')
        labels = {
            'customer': 'Khách hàng',
            'quantity1': 'Đá loại 1 (Tấn)',
            'quantity2': 'Đá loại 2 (Tấn)',
            'quantity3': 'Đá loại 3 (Tấn)',
            'quantity4': 'Đá loại 4 (Tấn)',
            'status': 'Tình trạng'
        }


class TicketFormCreate(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('customer', 'quantity1', 'quantity2', 'quantity3', 'quantity4')
        labels = {
            'customer': 'Khách hàng',
            'quantity1': 'Đá loại 1 (Tấn)',
            'quantity2': 'Đá loại 2 (Tấn)',
            'quantity3': 'Đá loại 3 (Tấn)',
            'quantity4': 'Đá loại 4 (Tấn)',
        }


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username',)
