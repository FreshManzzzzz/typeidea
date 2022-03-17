from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=50, widget=forms.widgets.Input(
        attrs={'class': 'form-control', 'style': "width:20%;"}
    ))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.widgets.EmailInput(
        attrs={'class': 'form-control', 'style': "width:40%;"}
    ))
    password1 = forms.CharField(label='Password', widget=forms.widgets.PasswordInput(
        attrs={'class': 'form-control', 'style': "width:40%;"}
    ))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.widgets.PasswordInput(
        attrs={'class': 'form-control', 'style': "width:40%;"}
    ))
    captcha = CaptchaField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username=username)
        if len(filter_result) > 0:
            raise forms.ValidationError('用户名已存在！')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('密码不匹配，请重新输入！')
        return password2

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
