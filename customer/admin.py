from django.contrib import admin
from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'institution_code', 'institution_name', 'customer_name', 'gender', 'customer_type', 'customer_duty', 'customer_title', 'customer_phone', 'approve_status', 'submit_date', )
    fields = ('institution_code', 'institution_name', 'customer_name', 'gender', 'customer_type', 'customer_duty', 'customer_title', 'customer_phone', 'approve_status', 'submit_date', )


admin.site.register(Customer, CustomerAdmin)
