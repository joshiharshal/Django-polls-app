"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import time
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse

START_TIME = time.time()


def health_check(request):
    return JsonResponse({"status": "healthy", "timestamp": time.time()})


def metrics(request):
    uptime = time.time() - START_TIME
    content = f"""# HELP django_polls_uptime_seconds Django Polls application uptime in seconds
# TYPE django_polls_uptime_seconds gauge
django_polls_uptime_seconds {uptime}
# HELP django_polls_healthy Django Polls app health status
# TYPE django_polls_healthy gauge
django_polls_healthy 1
"""
    return HttpResponse(content, content_type="text/plain; version=0.0.4")


urlpatterns = [
    path("", TemplateView.as_view(template_name="polls/home.html"), name="home"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("health/", health_check, name="health_check"),
    path("metrics/", metrics, name="metrics"),
]
