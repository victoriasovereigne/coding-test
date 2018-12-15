from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah', views.tambah, name='tambah'),
    # path('get-tambah-form', views.get_tambah_form, name='get_tambah_form'),
    path('detil/<int:data_id>', views.detil, name='detil')
]