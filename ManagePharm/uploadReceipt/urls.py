from django.urls import path
from . import views

urlpatterns = [
    path('upload-receipt/', views.upload_receipt_view, name='upload_receipt'),
    path('success/', views.receipt_success_view, name='receipt_success'),
]