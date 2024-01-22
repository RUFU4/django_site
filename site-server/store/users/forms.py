from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'email-ph', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password-ph', 'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ['username','password']
        
class UserRegistraterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'un-reg-ph', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password-ph', 'placeholder': 'Пароль'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'fn-reg-ph', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'ln-reg-ph', 'placeholder': 'Фамилия'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'id': 'email-reg-ph', 'placeholder': 'Адрес почты'}))
    shipping_adress = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'address-reg-ph', 'placeholder': 'Адрес доставки'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'postal-reg-ph', 'placeholder': 'Почтовый код'}))
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'shipping_address', 'postal_code']

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'name-account'}))
    shipping_address = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'addres-account'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'id': 'email-account'}))   

    class Meta:
        model = User
        fields = ['email', 'username', 'shipping_address'] 