from django.contrib import admin
from .models import ResumeData, Contact, CoverLetter

# Register your models here.
admin.site.register(Contact)
admin.site.register(ResumeData)
admin.site.register(CoverLetter)
