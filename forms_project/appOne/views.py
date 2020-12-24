from django.shortcuts import render
from appOne import forms
# Create your views here.


def index(request):
    return render(request, 'appOne/index.html')

def form_name_view(request):
    form = forms.formName()

    if request.method == 'POST':
        form = forms.formName(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE
            print('validation successfull')
            print(form.cleaned_data['name'])        
            print(form.cleaned_data['email']) 
            print(form.cleaned_data['text']) 

    return render(request, 'appOne/forms_page.html', {'form':form})

