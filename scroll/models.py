from django.db import models

class ScrollSlider(models.Model):
    img = models.ImageField(upload_to='sliderimg/')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.CharField(max_length=250, verbose_name='Текст')
    css = models.CharField(max_length=250, null=True, default='-', verbose_name='Осн. картинка?')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Слайд'
        verbose_name_plural = 'Слайды'
