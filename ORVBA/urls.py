from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ORVBA.views import *

urlpatterns=[
    # path("login/",SigninView.as_view(),name="sign_in"),
    # path("signup/",SignupView.as_view(),name="sign_up"),

    


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)