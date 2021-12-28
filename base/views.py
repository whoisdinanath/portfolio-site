from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import *
from django.core.mail import send_mail
from django.urls import reverse_lazy



class HomeTemplateView(TemplateView):
    template_name = 'base/home.html'

    # override get context data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['skills'] = Skill.objects.all()
        context['works'] = RecentWork.objects.all()
        return context


def contact(request):
        
    if request.method == "POST":
        visitor_name = request.POST.get('name')
        visitor_email = request.POST.get('email')
        
        visitor_message = request.POST.get('message')
        
    context={'name':visitor_name, 'email':visitor_email, 'message':visitor_message}
    visitor=VisitorMessage(name=visitor_name, email=visitor_email, message=visitor_message)
    visitor.save()
    return render(request, 'base/home.html', context)
    