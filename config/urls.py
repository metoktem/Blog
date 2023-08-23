from django.contrib import admin
from django.urls import path
from MyApp.views import home_view_general, home_view_profile, login_view, register_view, postlist_view, create_post, PostDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Ana sayfa için URL
    path('', home_view_general, name='home'),

    # Giriş sayfası için URL
    path('giris/', login_view, name='giris'),

    # Çıkış sayfası için URL
    path('cikis/', home_view_general, name='cikis'),

    # Yeni kayıt sayfası için URL
    path('yenikayit/', register_view, name='yenikayit'),

    # Django admin paneli için URL
    path('admin/', admin.site.urls),

    # Post listesi için URL
    path('post_list/', postlist_view, name='post_list'),

    # Belirli bir postu silmek için URL
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('create_post/', create_post, name='create_post'),


    # Diğer URL tanımlamalarını burada ekleyebilirsiniz
]



