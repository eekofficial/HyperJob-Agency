from django.shortcuts import render
from django.views import View
from .models import Vacancy
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

class VacanciesView(View):
    def get(self, request):
        return render(request, 'vacancy/vacancy.html', {'vacancies': Vacancy.objects.all})

class NewVacancyView(View):
    def post(self, request):
        if not request.user.is_staff:
            return HttpResponse(status=403)
        Vacancy.objects.create(description=request.POST.get('description'), author=request.user)
        return redirect('/home')