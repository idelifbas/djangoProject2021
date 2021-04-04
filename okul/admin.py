from django.contrib import admin
from okul.models import Okul
from okul.models import İl
from okul.models import Öğretmen
from okul.models import Öğrenci
from okul.models import Sınıf

##Admin modeli oluşturma
class OkulAdmin(admin.ModelAdmin):  ##admin modeline özellikler ekliyoruz
    list_display = ['baslik','yayinlanmaTarihi'] ## list display modelde birden fazla özelliğin görünmesiini sağlar
    list_display_links = ['yayinlanmaTarihi'] ## görünen özelliklerin birden fazlasına link verir, modelinin detayına erişmek için.
    list_filter = ['yayinlanmaTarihi'] ##filtreleme özelliği tarih bilgimize göre
    search_fields = ['baslik','metin'] ## baslik ve metinde gecen verilere göre arama yapaar
    list_editable = ['baslik'] ##listelenen baslık verisini listeleme ekraında düzenlemeye izin verir. Not: display links e verilen veiler bu alana verilemez
    class Meta:
        model=Okul

# Register your models here.
admin.site.register(Okul,OkulAdmin)
admin.site.register(İl)
admin.site.register(Öğretmen)
admin.site.register(Öğrenci)
admin.site.register(Sınıf)