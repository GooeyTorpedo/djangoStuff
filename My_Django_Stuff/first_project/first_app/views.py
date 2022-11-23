from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Connect to database
from first_app.models import Topic, Webpage, AccessRecord

# def index(request):
#     return HttpResponse('hello world!')

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    # my_dict = {'insert_me': "hello i am from first_app/views.py"}
    return render(request, 'first_app/index.html', context= date_dict)
