from django.contrib.auth.forms import UserCreationForm


class RegisterCustomerForm(UserCreationForm):
    class Meta:
        field = ['email', 'username']
