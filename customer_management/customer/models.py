from datetime import timedelta

from django.core.validators import RegexValidator
from django.db import models


class Plan(models.Model):
    PLAN_CHOICES = [
        ('Platinum365', 'Platinum'),
        ('Gold180', 'Gold'),
        ('Silver90', 'Silver')
    ]

    PLAN_COST = {
        'Platinum365': 499,
        'Gold180': 299,
        'Silver90': 199
    }

    PLAN_VALIDITY = {
        'Platinum365': 365,
        'Gold180': 180,
        'Silver90': 90
    }

    PLAN_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ]

    name = models.CharField(max_length=50, choices=PLAN_CHOICES, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=PLAN_STATUS_CHOICES, default='Active')

    def save(self, *args, **kwargs):
        if self.name in self.PLAN_CHOICES:
            self.cost = self.PLAN_COST[self.name]
            self.validity = self.PLAN_VALIDITY[self.name]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    number = models.CharField(
        max_length=12,
        validators=[RegexValidator(regex='^\d{12}$', message='Number must be 12 digits')]
    )
    registration_date = models.DateField(auto_now_add=True)
    assigned_mobile_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^\d{10}$', message='Assigned Mobile Number must be 10 digits')]
    )
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    renewal_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.plan:
            self.renewal_date = self.start_date + timedelta(days=self.plan.validity)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.customer.name} - {self.plan.name}'
