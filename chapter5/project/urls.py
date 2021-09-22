from django.urls import path, include
from rest_framework import urlpatterns
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter

# blog_list = BlogViewSet.as_view({
#     'get' : 'list',
#     'post' : 'create'
# })

# blog_detail = BlogViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'delete' : 'destroy'
# })

# urlpatterns = [
#     path('blog/', blog_list),
#     path('blog/<int:pk>', blog_detail),
# ]


router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('blog', BlogViewSet)

urlpatterns =[
    path('', include(router.urls))
]