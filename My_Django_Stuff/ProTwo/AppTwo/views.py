from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users
from AppTwo import forms #or from AppTwo.forms import NewUserForm
# Create your views here.


# def index(request):
#     return HttpResponse('<em>My Second App</em>')
def index(request):
    return render(request, 'appTwo/index.html')

def user(request):
    user_list = Users.objects.order_by('fname')
    user_dict = {'user': user_list}
    return render(request, 'AppTwo/user.html', context= user_dict)


def help(request):
    my_dict = {'help_insert': 'This is the help page'}
    return render(request, 'AppTwo/help.html', context=my_dict)

def user_form_view(request):
    form = forms.userForm()

    if request.method == 'POST':
        form = forms.userForm(request.POST)

        if form.is_valid():
            form.save(commit =True)
            return index(request) #this will basically return to home page

        else:
            print('error form invalid!')

    
    return render(request, 'AppTwo/formpage.html', {'form': form})