from django.contrib import admin
from apps.products.models import Product, MeasureUnit, CategoryProduct, Indicator


admin.site.register(Product)
admin.site.register(MeasureUnit)
admin.site.register(CategoryProduct)
admin.site.register(Indicator)
