from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='blog-list'),
    path('blog/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)