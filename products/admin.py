from django.contrib import admin
from .models import Products,Offer


class ProductAdmin(admin.ModelAdmin):#this class will align  items products
    list_display = ('name','price','stock','description')
# Register your models here.



admin.site.register(Products,ProductAdmin)


class OfferAdmin(admin.ModelAdmin):#the class enables formatting/alignment of offer items on the admin page
    list_display = ('code','description','discount')
admin.site.register(Offer,OfferAdmin)