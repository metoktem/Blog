from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)  # Başlık alanı
    content = models.TextField(null=True, blank=True)  # İçerik alanı
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # İsteğe bağlı resim alanı
    description = models.TextField(max_length=50000)  # Açıklama alanı
    is_deleted = models.BooleanField(default=False)  # Silinmiş mi işareti
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturma tarihi (otomatik olarak eklenecek)
    updated_at = models.DateTimeField(auto_now=True)  # Güncelleme tarihi (otomatik olarak güncellenecek)

    def __str__(self):
        return self.title  # Nesne dizesi, başlık olarak döndürülür

