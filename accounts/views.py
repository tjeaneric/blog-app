from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from django.views import generic


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'




# class RegisterPage(FormView):
#     template_name = 'register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('home')

#     def form_valid(self,form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)


#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('home')
#         return super(RegisterPage, self).get(*args, **kwargs)
