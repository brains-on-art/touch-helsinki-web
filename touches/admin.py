from django.contrib import admin

# Register your models here.
from .models import Delta


class DeltaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Delta, DeltaAdmin)
