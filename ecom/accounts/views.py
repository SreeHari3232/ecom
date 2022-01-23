from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
class RegisterPage(SuccessMessageMixin, FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
         form.save()
         return super(RegisterPage, self).form_valid(form)
    
    success_message = 'Account Created Successfully!'
    
   
    

@login_required
def createProfile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully!!")
            form = ProfileForm(instance=profile)
            return redirect('login')
            
    context = {'form':form}
    return render(request, 'accounts/profile_create.html', context)



            
    
    
    
    
    
   
    

    
 
    
