from django.db import models

class StatusCrm(models.Model):
    order_status = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.order_status

    class Main():
        verbose_name='Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Main():
        verbose_name='Заказ'
        verbose_name_plural = 'Заказы'