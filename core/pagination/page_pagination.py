from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count

        return Response({
            'count': count,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'results': data
        })
