from django.http import HttpResponse
def contact(request):
     return  HttpResponse("this is contatct")
def home(request):
     return HttpResponse("this is home page")