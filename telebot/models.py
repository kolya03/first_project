from django.db import models

class TeleSettings(models.Model):
    tg_token =models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Айди чата')
    tg_message = models.TextField(verbose_name='Сообщение')
    def __str__(self):
        return self.tg_message

    class Main():
        verbose_name = 'telebot'
        verbose_name_plural = 'Настроить бота'
