from permissions import ReadOrAdminPermission
from rest_framework import filters, mixins, viewsets
class ListCreateDestroyMixins(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = (ReadOrAdminPermission,)
