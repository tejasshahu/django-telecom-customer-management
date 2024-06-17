from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

from .forms import CustomerRegistrationForm, SubscriptionForm
from .models import Customer, Subscription


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.all()


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscription'] = Subscription.objects.filter(customer=self.object).first()
        return context


class RegisterCustomerView(CreateView):
    model = Customer
    form_class = CustomerRegistrationForm
    template_name = 'customer/customer_registration.html'

    def form_valid(self, form):
        customer = form.save()
        return redirect(reverse('choose_plan', args=[customer.id]))


class ChoosePlanView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'customer/choose_plan.html'

    def get_initial(self):
        customer = get_object_or_404(Customer, pk=self.kwargs['customer_id'])
        try:
            subscription = Subscription.objects.get(customer=customer)
            initial = {
                'plan': subscription.plan
            }
        except Subscription.DoesNotExist:
            initial = {}
        return initial

    def form_valid(self, form):
        subscription = form.save(commit=False)
        customer = get_object_or_404(Customer, pk=self.kwargs['customer_id'])
        existing_subscription = Subscription.objects.filter(customer=customer).first()
        if existing_subscription:
            existing_subscription.plan = subscription.plan
            existing_subscription.start_date = timezone.now().date()
            existing_subscription.save()
        else:
            subscription.customer = customer
            subscription.start_date = timezone.now().date()
            subscription.save()
        return redirect('customer_list')
