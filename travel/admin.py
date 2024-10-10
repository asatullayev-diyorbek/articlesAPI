from django.contrib import admin

from .models import Class, Hotel, Travel


class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


class HotelAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'price')


class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'period_amount', 'period_unit', 'price', 'travel_class', 'hotel')


admin.site.register(Class, ClassAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Travel, TravelAdmin)