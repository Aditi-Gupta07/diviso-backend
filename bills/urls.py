from django.urls import path
from .views import BillUploadView

urlpatterns = [
    path('upload/', BillUploadView.as_view(), name='bill-upload'),
]