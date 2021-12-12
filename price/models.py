from django.db import models

class PriceCard(models.Model):
    pc_value = models.CharField(max_length=50, verbose_name='Цена карты')
    pc_description = models.CharField(max_length=250, verbose_name='Описание')
    def __str__(self):
        return self.pc_value

    class Main():
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

class PriceTable(models.Model):
    pt_service = models.CharField(max_length=250, verbose_name='Услуга')
    pt_old_price = models.CharField(max_length=250, verbose_name='Старая цена')
    pt_new_price = models.CharField(max_length=250, verbose_name='Новая цена')
    def __str__(self):
        return self.pt_service

    class Main():
        verbose_name = 'Услуга'
        verbose_name_plurak = 'Услуги'
