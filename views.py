from django.shortcuts import render
from users.models import *
from django.views.generic import View

class Users(View):
        
    def get(self, request):
        users = User.objects.all()
        return render(request, 'index.html', { 'users': users })