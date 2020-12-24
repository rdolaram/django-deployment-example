from django.shortcuts import render
#from django.http import HttpResponse
#from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

#Views is a request handler function
#which receives HTTP requests and returns HTTP responses



def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    form = NewUserForm()
    #When somebody inputs information on the form
    #and we receive that information.
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            #Line under commits the form to the database. 
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'appTwo/users.html', {'form':form})

