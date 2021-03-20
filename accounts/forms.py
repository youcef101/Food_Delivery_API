from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Customer

class CreateNewUser(UserCreationForm):
    class Meta:
      model=User
      fields=['username','first_name','last_name','email','password1','password2']
class ProfileUpdate(ModelForm):
  class Meta:
    model=Customer
    fields=['sexe','phone','adresse','image']

class UserUpdate(ModelForm):
  class Meta:
    model=User
    fields=['first_name','last_name','email']