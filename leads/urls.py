from django.urls import path
from .views import delete, LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_index'),
    path('new', LeadCreateView.as_view(), name='lead_new'),
    path('<pk>', LeadDetailView.as_view(), name='lead_show'),
    path('<pk>/update', LeadUpdateView.as_view(), name='lead_update'),
    path('<pk>/delete', LeadDeleteView.as_view(), name='lead_delete')
]