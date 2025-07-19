from rest_framework.pagination import LimitOffsetPagination

class SimpleOptionalPagination(LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if 'limit' in request.query_params or 'offset' in request.query_params:
            return super().paginate_queryset(queryset, request, view)
        return None