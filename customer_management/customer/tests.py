from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Customer, Plan, Subscription


class CustomerModelTests(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name='John Doe',
            dob='1990-01-01',
            email='john@example.com',
            number='123456789012',
            assigned_mobile_number='9876543210'
        )
        self.plan = Plan.objects.create(
            name='Platinum365',
            cost=499.00,
            validity=365,
            status='Active'
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.email, 'john@example.com')

    def test_plan_creation(self):
        self.assertEqual(self.plan.name, 'Platinum365')
        self.assertEqual(self.plan.cost, 499.00)

    def test_subscription_creation(self):
        subscription = Subscription.objects.create(
            customer=self.customer,
            plan=self.plan,
            start_date=timezone.now().date(),
            renewal_date=timezone.now().date() + timedelta(days=self.plan.validity)
        )
        self.assertEqual(subscription.customer, self.customer)
        self.assertEqual(subscription.plan, self.plan)
        self.assertEqual(subscription.renewal_date, subscription.start_date + timedelta(days=self.plan.validity))


class CustomerViewsTests(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name='Jane Doe',
            dob='1992-02-02',
            email='jane@example.com',
            number='098765432109',
            assigned_mobile_number='1234567890'
        )
        self.plan = Plan.objects.create(
            name='Gold180',
            cost=299.00,
            validity=180,
            status='Active'
        )

    def test_register_customer_view(self):
        response = self.client.post(reverse('register_customer'), {
            'name': 'Alice Doe',
            'dob': '1995-05-05',
            'email': 'alice@example.com',
            'number': '112233445566',
            'assigned_mobile_number': '6677889900'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('choose_plan', args=[Customer.objects.last().id]))

    def test_choose_plan_view(self):
        response = self.client.post(reverse('choose_plan', args=[self.customer.id]), {
            'plan': self.plan.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('customer_list'))

        subscription = Subscription.objects.get(customer=self.customer)
        self.assertEqual(subscription.plan, self.plan)
        self.assertEqual(subscription.renewal_date, subscription.start_date + timedelta(days=self.plan.validity))

    def test_modify_plan(self):
        subscription = Subscription.objects.create(
            customer=self.customer,
            plan=self.plan,
            start_date=timezone.now().date(),
            renewal_date=timezone.now().date() + timedelta(days=self.plan.validity)
        )
        new_plan = Plan.objects.create(
            name='Silver90',
            cost=199.00,
            validity=90,
            status='Active'
        )
        response = self.client.post(reverse('choose_plan', args=[self.customer.id]), {
            'plan': new_plan.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('customer_list'))

        subscription.refresh_from_db()
        self.assertEqual(subscription.plan, new_plan)
        self.assertEqual(subscription.renewal_date, subscription.start_date + timedelta(days=new_plan.validity))
