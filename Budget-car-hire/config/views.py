from django.views.generic import TemplateView
# from django.contrib.auth.views import LoginView, LogoutView



class IndexView(TemplateView):
    template_name = 'index.html'




