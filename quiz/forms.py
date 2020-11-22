from django import forms
from django.forms.widgets import RadioSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Your first name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Your last name')
    email = forms.EmailField(max_length=256, help_text='Your email id (e.g. foo@example.com')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')