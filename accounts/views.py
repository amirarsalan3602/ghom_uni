from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


class LoginView(View):
    def post(self, request):
        user = authenticate(request, username=request.POST.get('username'),
                            password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return HttpResponse('کاربر با موفقیت لاگین شد')
        else:
            return HttpResponse("نام کاربری یا رمز عبور اشتباه است")


class RegisterUser(View):
    def get(self, request):
        return render(request, 'register.html')
