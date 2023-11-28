from django.db import models

# Create your models here.
class ToolAttachment(models.Model):
    function_name = models.CharField(max_length=50, unique=True, help_text="Unique identifier for the tool's function")
    template_name = models.CharField(max_length=100, help_text="Template path for the tool's function")

    def __str__(self):
        return self.function_name