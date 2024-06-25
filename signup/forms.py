from django import forms
from .models import CustomUser, MyPage

class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'major', 'nickname', 'password', 'phone_number')
        widgets = {
            'password' : forms.PasswordInput(),
        }

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class MyPageForm(forms.ModelForm):
    class Meta:
        model = MyPage
        fields = ('introduction', 'mbti', 'hobby', 'favorite_foods')