from django import forms

from .models import Customer, Subscription, Plan


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'dob', 'email', 'number', 'assigned_mobile_number']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['plan']

    plan = forms.ModelChoiceField(queryset=Plan.objects.filter(status='Active'), required=True)
