from django.db import models

class Artiles(models.Model):
    title = models.CharField('Title', max_length=50 ,)
    anons = models.CharField('anons', max_length=250 ,)
    full_text = models.TextField('article')
    data = models.DateTimeField('Data and time')
    
    def __str__ (self):
        return self.title
    
    class Meta: 
        verbose_name = 'New'
        verbose_name_plural = 'News'