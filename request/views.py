from user.permissions import IsMasterUser
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Request
from .permissions import IsNewRequest
from .serializers import ReguestForMasterSerializer, ReguestForUserSerializer


class RequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet for create, update and delete Request by user.
    """

    serializer_class = ReguestForUserSerializer

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsNewRequest]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RequestListRetrieveViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `update`, and `list` actions.
    """
    
    queryset = Request.objects.all()
    serializer_class = ReguestForMasterSerializer
    permission_classes = [IsMasterUser]
