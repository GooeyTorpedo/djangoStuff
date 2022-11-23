from django import forms
from AppTwo.models import Users

class userForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=128)
    # last_name = forms.CharField(max_length=128)
    # email = forms.EmailField()
    class Meta:
        model = Users
        fields = "__all__"
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }