from django.urls import path,include
from terminal.views import home_view,receive_data,send_data
from django.urls import path



urlpatterns = [
    path('home/', home_view, name='home'),
    path('send_data/', send_data, name='send_data'),
    path('receive_data/', receive_data, name='receive_data'),
]