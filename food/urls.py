from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:item_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('edit/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete')
]
