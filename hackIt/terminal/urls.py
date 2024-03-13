from django.urls import path
from terminal.views import TerminalView


urlpatterns = [
    path('',TerminalView.as_view(),name = 'terminal_commands'),
]