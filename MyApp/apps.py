from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Varsayılan otomatik alan türü
    name = 'MyApp'  # Uygulama adı
