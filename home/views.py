from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import CommentModel


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class CommentsView(View):
    def post(self, request):
        if request.user.is_authenticated:
            CommentModel.objects.create(user=request.user, name=request.POST.get('name'),
                                        subject=request.POST.get('subject'), recipient=request.POST.get('recipient'),
                                        message=request.POST.get('message'))
            return HttpResponse('نظر شما با موفقیت ثبت شد')
        else:
            return HttpResponse("برای ثبت نظر لطفاً وارد شوید")
