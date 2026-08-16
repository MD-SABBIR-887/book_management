from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.BookList)
admin.site.register(models.Review)