from django.contrib import admin
from django.urls import reverse_lazy

from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Profile)

admin.site.logout_url = reverse_lazy('logout')
