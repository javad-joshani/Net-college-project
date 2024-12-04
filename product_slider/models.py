from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=55,verbose_name="عنوان")
    image = models.ImageField(upload_to='sliders',verbose_name="عکس")
    link = models.URLField()
    order = models.PositiveIntegerField(null=True,blank=True,unique=True,verbose_name="ترتیب")
    
    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = "اسلاید ها"
        ordering = ['order']
        
    def save(self,*args,**kwargs):
        if self.order == None:
            last = self.__class__.objects.last()
            self.order = last.order + 1

        super().save(*args,**kwargs)
        
