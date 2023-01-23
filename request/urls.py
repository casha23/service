from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    InvoiceCreateListRetrieveUpdateViewSet, InvoiceForUserList, RequestListRetrieveUpdateViewSet, RequestViewSet
    )

router = DefaultRouter()
router.register(r'requests', RequestViewSet, basename='request-for-user')
router.register(r'master-requests', RequestListRetrieveUpdateViewSet, basename='request-for-master')
router.register(r'invoices', InvoiceCreateListRetrieveUpdateViewSet, basename='invoice-for-master')

urlpatterns = [
    path('', include(router.urls)),
    path('user-invoices/', InvoiceForUserList.as_view(), name='invoice-list-for-user')
]
