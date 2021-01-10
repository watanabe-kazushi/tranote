from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    form = UserCreationForm()
    if form.is_vaild():
        form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'account/login.html',{'form':form})
