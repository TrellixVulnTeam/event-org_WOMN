from django.contrib import admin

from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'city', 'country', 'phonenumber', 'birth_date')

admin.site.register(Profile, ProfileAdmin)
