from django.db import models


class Plan3(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    price_monthly = models.CharField(max_length=30, blank=True, null=True)
    price_yearly = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, default='ایمیل اختصاصی', blank=True, null=True)
    frame = models.CharField(max_length=30, default='قالب', blank=True, null=True)
    prodc = models.CharField(max_length=30, default='محصول', blank=True, null=True)
    imgforpro = models.CharField(max_length=30, blank=True, null=True, default='تصویر برای هر محصول')
    Bandwidth = models.CharField(max_length=30, blank=True, null=True, default='پهنای باند')
    support = models.CharField(max_length=30, blank=True, null=True, default='پشتیبانی 24 ساعته')

    def __str__(self):
        return self.title
