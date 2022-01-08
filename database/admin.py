from django.contrib import admin
from .models import TermCs, Blog, TermSe, BugReport

# Register your models here.

admin.site.register(TermCs)
admin.site.register(Blog)
admin.site.register(TermSe)
admin.site.register(BugReport)
