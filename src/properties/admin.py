from django.contrib import admin

# Register your models here.
from .models import Property_Information,PropertyImage

class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage

@admin.register(Property_Information)
class Property_Information_Admin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

    class Meta:
        model = Property_Information

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    pass
