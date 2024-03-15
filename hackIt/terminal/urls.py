from django.urls import path,include
from terminal.views import TerminalView


urlpatterns = [
    path('',TerminalView.as_view(),name = 'terminal_commands'),
    path('authentication/', include('user.urls')),


]