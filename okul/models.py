from django.db import models

# Create your models here.
class Okul(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Başlık') #charfield (karakter alani) icin maximum boyutu mutlaka belirtmeliyiz
    metin = models.TextField(verbose_name='Metin') # textfield çok uzun yazilar için kullanir, boyut belirtmeye gerek yok
    yayinlanmaTarihi = models.DateTimeField(verbose_name='Yayınlanma Tarihi') #tarih ve saat bilgisini alir.

#verbose_name kullanıcaya nasıl görünmesini istiyorsun


    def __str__(self):
        return self.baslik  ##her objenin adı baslık değişkeninde ki değer olarak görünsün.

class İl(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Başlık')
    metin = models.TextField(verbose_name='Metin')
    yayinlanmaTarihi = models.DateTimeField(verbose_name='Yayınlanma Tarihi')

    def __str__(self):
        return self.baslik

class Öğretmen(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Başlık')
    metin = models.TextField(verbose_name='Metin')
    yayinlanmaTarihi = models.DateTimeField(verbose_name='Yayınlanma Tarihi')

    def __str__(self):
        return self.baslik


class Öğrenci(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Başlık')
    metin = models.TextField(verbose_name='Metin')
    yayinlanmaTarihi = models.DateTimeField(verbose_name='Yayınlanma Tarihi')

    def __str__(self):
        return self.baslik


class Sınıf(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Başlık')
    metin = models.TextField(verbose_name='Metin')
    yayinlanmaTarihi = models.DateTimeField(verbose_name='Yayınlanma Tarihi')

    def __str__(self):
        return self.baslik