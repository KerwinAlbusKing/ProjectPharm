from django.urls import path
from . import views

urlpatterns = [
    path('list', views.item_list, name='item_list'),               # Read: 목록 보기
    path('create/', views.item_create, name='item_create'),    # Create: 새 항목 추가
    path('<str:insurance_code>/edit/', views.item_update, name='item_update'),  # Update: 항목 수정
    path('<str:insurance_code>/delete/', views.item_delete, name='item_delete'),  # Delete: 항목 삭제
]
