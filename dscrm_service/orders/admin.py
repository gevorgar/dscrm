from django.contrib import admin

from services.models import ServiceItem
from .models import Order


class PriceAdminInline(admin.TabularInline):
    model = ServiceItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'device', 'order_description', 'created_dt', 'last_updated_dt', 'order_status')
    search_fields = ('device__id', 'device__serial_number')
    inlines = (PriceAdminInline,)


admin.site.register(Order, OrderAdmin)
