from django.urls import path

from apps.user.views import buyer_registration, user_login, check

urlpatterns = [
    path('buyer-registration/', buyer_registration, name='B_reg'),
    path('login/', user_login, name='login'),
    path('check/', check),
]