from rest_framework import viewsets
from API.serializers import PostSerializer
from .models import Post
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import APIException




class CustomException(APIException):
    status_code = None
    detail = None
    default_detail = None

    def __init__(self, status_code, detail):
        CustomException.detail = detail
        CustomException.status_code = status_code



class CustomPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100
    min_limit = 1
    min_offset = 1
    max_offset = 50



class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ['title']
    ordering_fields = ['title']
    ordering = ['title']


    def get_queryset(self):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        order = self.request.query_params.get('ordering')
        limit = self.request.query_params.get('limit')


        if order:
            if order == 'title' or order == '-title':
                queryset = Post.objects.order_by(order)
                serializer = PostSerializer(queryset, many=True)
                return queryset
            else:
                raise CustomException(404, f'Value {order} is not availiable as ordering parameter, please try title or -title')

        elif limit:
            if limit.lstrip('-').isdigit():
                limit = int(limit)
                if limit <= 0:
                    raise CustomException(404, f'Value {limit} is not availiable as a limit parameter, please try a number more than zero')
                elif limit >= 100:
                    raise CustomException(404, f'Value {limit} is not availiable as a limit parameter, please try a number lower than 100')
            else:
                raise CustomException(404, f'Value {limit} is not availiable as a limit parameter, please try a number')


        return queryset


















