from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display= ('name', 'criminal_number', 'nickname', 'address', 'date_of_crime', 'arrest_date', 'occupation', 'crime_type', 'age', 'fathers_name', 'gender', 'wanted')

# Register your models here.
# admin.site.register(Criminal)
admin.site.register(Criminal, BookAdmin)

