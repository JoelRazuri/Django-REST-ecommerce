from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from django.db import models


class MeasureUnit(BaseModel):
    description = models.CharField('Descripción', max_length=100, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'


class CategoryProduct(BaseModel):
    description = models.CharField('Descripción', max_length=100, blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'


class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0, verbose_name='Porcentaje de descuento')
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return f'Oferta de la categoría {self.category_product}: {self.descount_value}%'

    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'


class Product(BaseModel):
    name = models.CharField('Nombre del producto', max_length=150, blank=False, null=False, unique=True)
    description = models.TextField('Descripción del producto', max_length=500, blank=False, null=False)
    image = models.ImageField('Imagen del producto', upload_to='products/', null=True, blank=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'