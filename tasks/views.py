from django.contrib.auth.models import User
from django.contrib import messages
# from django.http import request
from django.views.generic.edit import View
from django.shortcuts import redirect, render
from .forms import GenerateRandomUserForm
from tasks.tasks import create_random_user_accounts


class GenerateRandomUserView(View):
    template_name = 'tasks/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def get(self, request):
        user = User.objects.all()
        context = {
            'user' : user,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        total = int(request.POST.get('total'))

        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('create_user')

class ListUser(View):
    template_name = 'tasks/user_list.html'
    form_class = GenerateRandomUserForm
    def get(self, request):
        user = User.objects.all()
        context = {
            'user' : user,
        }
        return render(request, self.template_name, context)
