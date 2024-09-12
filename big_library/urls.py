from django.urls import path
from big_library import views

from big_library.apps import BigLibraryConfig

app_name = BigLibraryConfig.name

urlpatterns = [
    path('', views.DocumentListView.as_view(), name='document_list'),
    path('new/', views.DocumentCreateView.as_view(), name='document_create'),
    path('<int:pk>/', views.DocumentDetailView.as_view(), name='document_detail'),
    path('<int:pk>/edit/', views.DocumentUpdateView.as_view(), name='document_update'),
    path('<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document_delete'),
]
