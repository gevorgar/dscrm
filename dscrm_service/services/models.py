from django.db import models

from orders.models import Order


class Service(models.Model):
    """Услуга"""

    class Meta:
        db_table = "services"
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    name = models.CharField(verbose_name="Наименование услуги", max_length=20)
    warranty = models.IntegerField(verbose_name='Гарантия/дней')

    def __str__(self):
        return f"{self.name}"


class ServiceItem(models.Model):
    """Добавляемые услуги"""

    class Meta():
        verbose_name = 'Услуга в заказе'
        verbose_name_plural = 'Услуги в заказе'
        ordering = ['id']

    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    price = models.IntegerField(verbose_name='Стоимость', default='100')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='Заказ', blank=True, null=True)

    def __str__(self):
        return str(self.service)
