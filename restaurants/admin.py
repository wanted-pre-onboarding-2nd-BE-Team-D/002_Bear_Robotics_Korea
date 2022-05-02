from django.contrib import admin
from .models import Restaurant,Subsidary,Menu,Ward,Neighborhood

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Subsidary)
admin.site.register(Menu)
admin.site.register(Ward)
admin.site.register(Neighborhood)