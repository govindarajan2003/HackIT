from django.urls import path,include
from terminal.views import home_view,receive_data,send_data,download_terminal_record,receiver_view
from django.urls import path



urlpatterns = [
    path('home/', home_view, name='home'),
    path('send_data/', send_data, name='send_data'),
    path('receive_data/', receive_data, name='receive_data'),
    path('receiver/', receiver_view, name='receiver'),
    path('download/<int:id>/',download_terminal_record, name='download_terminal_record'),
]