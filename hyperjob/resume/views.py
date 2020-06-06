from django.shortcuts import render
from django.views import View
from .models import Resume
from django.shortcuts import redirect
from django.http import HttpResponse

class ResumesView(View):
    def get(self, request):
        return render(request, 'resume/resume.html', {'resumes': Resume.objects.all})

class NewResumeView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponse(status=403)
        Resume.objects.create(description=request.POST.get('description'), author=request.user)
        return redirect('/home')