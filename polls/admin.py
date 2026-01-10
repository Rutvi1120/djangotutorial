from django.contrib import admin
from .models import Question, Choice

# This tells Django that these models should have an admin interface
admin.site.register(Question)
admin.site.register(Choice)

