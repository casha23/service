from django_filters.rest_framework import DjangoFilterBackend
from user.permissions import IsMasterUser
from rest_framework import filters, generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Invoice, Request
from .permissions import IsNewRequest, IsUnpaidInvoice
from .serializers import (
    InvoiceSerializer, ReguestForMasterSerializer, ReguestForUserSerializer
    )

# APIs for Request

class RequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet for create, update and delete Request by user.
    """

    serializer_class = ReguestForUserSerializer

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsNewRequest]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RequestListRetrieveUpdateViewSet(mixins.ListModelMixin,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `update`, and `list` actions.
    """
    
    queryset = Request.objects.all()
    serializer_class = ReguestForMasterSerializer
    permission_classes = [IsMasterUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'phone_model', 'status']
    search_fields = ['problem_description']


# APIs for Invoice

class InvoiceCreateListRetrieveUpdateViewSet(mixins.CreateModelMixin,
                                             mixins.ListModelMixin,
                                             mixins.RetrieveModelMixin,
                                             mixins.UpdateModelMixin,
                                             viewsets.GenericViewSet):
    """
    A viewset that provides `create`, `retrieve`, `update`, and `list` actions.
    """
    
    queryset = Invoice.objects.all().select_related('master', 'request__user')
    serializer_class = InvoiceSerializer

    def get_permissions(self):
        if self.action in {'partial_update', 'update'}:
            permission_classes = [IsMasterUser, IsUnpaidInvoice]
        else:
            permission_classes = [IsMasterUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(master=self.request.user)


class InvoiceForUserList(generics.ListAPIView):
    """
    List with invoices for user
    """
    
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.select_related('request__user').filter(request__user=self.request.user)
