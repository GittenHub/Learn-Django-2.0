from django import forms
from django.contrib import auth
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', required=True, 
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入用户名'})) 
    # label可定制html中的label标签; required=True表示这个字段一定要填写才能提交
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'请输入密码'})) 
    # widget=forms.PasswordInput可定义在HTML中生成password类，以密文的形式隐藏密码.widget可定义这个form中一个字段的类型
    
    # 验证用户名密码是否正确
    def clean(self):
    # views.py中在进行.is_valid()，进行判断LoginForm是否有效时会使用这个方法
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password) 
        # .authenticate中的第一个参数request是可以不需要的
        if user is None:   
            raise forms.ValidationError('用户名或密码不正确')
            # 抛出错误raise
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data
            
class RegForm(forms.Form):
    username = forms.CharField(label='用户名', required=True, 
                               max_length=30,
                               min_length=3,
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入3-30位用户名'})) 
    email = forms.EmailField(label='邮箱', required=True, 
                               widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'请输入邮箱'})) 
    password = forms.CharField(label='密码', 
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'请输入密码'})) 
    password_again = forms.CharField(label='再输入一次密码',
                                     min_length=6,
                                     widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'再输入一次密码'}))

    def clean_username(self): # clean加下划线加字段名称，可专门针对这个字段进行验证
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self): 
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次输入的密码不一致')
        return password_again