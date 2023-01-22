from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import RequestListRetrieveViewSet, RequestViewSet


router = DefaultRouter()
router.register(r'requests', RequestViewSet, basename='request-for-user')
router.register(r'master-requests', RequestListRetrieveViewSet, basename='request-for-master')

urlpatterns = [
    path('', include(router.urls)),
]