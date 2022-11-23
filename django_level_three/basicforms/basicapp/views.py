from django.shortcuts import render
from basicapp import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    # check request method is POST
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        # .is_valid() is a boolean check to see if form is valid
        if form.is_valid():
            print('VALIDATION SUCCESS!')
            print("Name: " + form.cleaned_data['name']) #fields in forms.py inside []
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})