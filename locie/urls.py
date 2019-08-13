from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.urls import path

urlpatterns = [
            path('login/',views.index, name="index"),
            path('',views.login, name="login"),
            
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
