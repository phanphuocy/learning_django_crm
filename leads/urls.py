from django.urls import path
from .views import index, show, new, update, delete

app_name = 'leads'

urlpatterns = [
    path('', index, name='list_index'),
    path('new', new, name='list_new'),
    path('<pk>', show, name='list_show'),
    path('<pk>/update', update, name='list_update'),
    path('<pk>/delete', delete, name='list_delete')
]