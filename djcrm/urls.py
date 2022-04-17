from django.contrib import admin
from django.urls import path, include
from leads.views import LeadListView

urlpatterns = [
    path('', LeadListView.as_view()),
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads'))
]
