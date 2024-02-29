from django import forms
from django.core.exceptions import ValidationError

from liberty_market.models import Item, Author, Order


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'category','author', 'price', 'royalties', 'ends_in', 'owner_full_name',
                  'owner_user_name', 'image']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=28)
    password = forms.CharField(max_length=28, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=28, widget=forms.TextInput(
        attrs={"id": "password", "type": "password"}))
    password2 = forms.CharField(max_length=28, widget=forms.TextInput(
        attrs={"id": "password", "type": "password"}))

    def save(self, commit=True):
        user = super().save(commit)
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Passwords must be match")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Author
        fields = ("username", "first_name", "last_name", "password1", "password2", "image")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["item"]