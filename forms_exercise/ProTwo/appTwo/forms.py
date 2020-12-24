from django import forms
from appTwo.models import User



#We would use ModelForm instead of Form because we are
#connecting the form to a model.
class NewUserForm(forms.ModelForm):
    #Python3 allows Meta. You could also have Meta()
    class Meta:
        #This should always be called model
        model = User
        fields = '__all__'

    
