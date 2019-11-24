from django.contrib import admin

# Register your models here.
from .models import Gift, Swap, Profile

# class SistaRegiftaAdmin(admin.ModelAdmin):  # add this
#       list_display = ('title', 'description', 'completed')

admin.site.register(Gift)
admin.site.register(Swap)
admin.site.register(Profile)


