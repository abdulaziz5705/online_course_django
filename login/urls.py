from django.urls import path
from .views import login_view, regester_view, log_out, account


urlpatterns = [
    path('login/', login_view, name='login'),
    path('regester/', regester_view, name='regester'),
    path('log_out/', log_out, name='log_out'),
    path('account/', account, name='account')


]
