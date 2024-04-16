from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['email'].label = '이메일'

    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            'email',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text