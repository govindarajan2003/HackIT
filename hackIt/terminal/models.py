from django.db import models
from utils.constants import generate_status_choices
from user.models import User

class TerminalCommands(models.Model):
    command = models.CharField(max_length = 100)
    action = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

    def __str__(self):
        return f"{self.command} - {self.action} - Created: {self.created_at} - Updated: {self.updated_at}"
    

class Records(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'user_record')
    terminal_command = models.ForeignKey(TerminalCommands,on_delete = models.CASCADE, related_name = 'command_record' )
    url = models.CharField(max_length = 100)
    status = models.CharField(choices = generate_status_choices(), default = generate_status_choices()[0], max_length = 20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.command} - {self.URL} - Status: {self.status} - Created: {self.created_at} - Updated: {self.updated_at}"