from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.core.mail import send_mail
from Systango_Project.settings import EMAIL_HOST_USER

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            email = request.POST['email']
            send_mail(
                'Username and Password',
                'Dear User your account has been created.\nPlease find your username and password below to login on the website.\n\nUsername: {}\nPassword: {}\n\nTeam '.format(username,password),
                EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
        return render(request, 'registration/registration.html', {'form': form})
