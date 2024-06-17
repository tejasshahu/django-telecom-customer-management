# Django Telecom Customer Management

This is a Django-based web application for managing telecom customers and their subscription plans. 
It allows users to register customers, choose a plan, and upgrade or downgrade existing plans. 
The home page displays customer details along with their current plan.

## Features

- Customer registration
- Plan selection (Platinum365, Gold180, Silver90)
- Plan upgrade/downgrade
- View customer details with plan and renewal date

## Project Structure
customer_management/
│
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── customer_management/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
└── customer/
├── init.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests.py
├── views.py
├── templates/
│ └── customer/
│     ├── customer_detail.html
│     ├── customer_list.html
│     ├── customer_registration.html
│     └── choose_plan.html
└── migrations/

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tejasshahu/django-telecom-customer-management.git
    cd django-telecom-customer-management
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

3. Run migrations:

    ```bash
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    ```

4. Create a superuser:

    ```bash
    docker-compose run web python manage.py createsuperuser
    ```

5. Access the application:

    Open your web browser and go to `http://localhost:8000`.

## Models

### Plan

- `name` (choices: 'Platinum365', 'Gold180', 'Silver90')
- `cost` (choices: 499, 299, 199)
- `validity` (days: 365, 180, 90)
- `status` (choices: 'Active', 'Inactive')

### Customer

- `name`
- `dob`
- `email`
- `number` (12 digits)
- `assigned_mobile_number` (10 digits)
- `registration_date`

### Subscription

- `customer` (ForeignKey to Customer)
- `plan` (ForeignKey to Plan)
- `start_date`
- `renewal_date`

## Usage

1. **Register a Customer**:

   Go to `http://localhost:8000/register/` and fill in the customer details.

   

2. **Choose a Plan**:

   After registration, you will be redirected to the plan selection page. Choose a plan for the customer.

3. **View Customer Details**:

   The home page displays a list of customers along with their current plan and renewal date.

4. **Modify Plan**:

   Go to the customer's detail page and select a new plan if needed. The renewal date will be updated accordingly.

## Running Tests

To run the tests, use:

```bash
docker-compose run web python manage.py test customer
```

Author
Tejas Shahu
https://github.com/tejasshahu