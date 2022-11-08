from django.urls import path

from apps.user.views import buyer_registration, user_login, seller_registration, user_logout

urlpatterns = [
    path('buyer-registration/', buyer_registration, name='B_reg'),
    path('seller-registration/', seller_registration, name='S_reg'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]