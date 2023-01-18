from core.enums.choice_enum import ChoiceEnum

from apps.orders.models import OrderModel

import django_filters
from django_filters import OrderingFilter
from django_filters import rest_framework as filters


class OrderFilter(filters.FilterSet):
    order_by_field = 'order'
    order = OrderingFilter(
        fields=(
            ('name', 'name'), ('-name', '-name'),
            ('id', 'id'), ('-id', '-id'),
            ('surname', 'surname'), ('-surname', '-surname'),
            ('email', 'email'), ('-email', '-email'),
            ('phone', 'phone'), ('-phone', '-phone'),
            ('age', 'age'), ('-age', '-age'),
            ('course', 'course'), ('-course', '-course'),
            ('course_format', 'course_format'), ('-course_format', '-course_format'),
            ('course_type', 'course_type'), ('-course_type', '-course_type'),
            ('sum', 'sum'), ('-sum', '-sum'),
            ('status', 'status'), ('-status', '-status'),
            ('alreadyPaid', 'alreadyPaid'), ('-alreadyPaid', '-alreadyPaid'),
            ('group', 'group'), ('-group', '-group'),
            ('created_at', 'created_at'), ('-created_at', '-created_at'),
            ('manager', 'manager'), ('-manager', '-manager'),
        )
    )

    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    phone = filters.CharFilter(field_name='phone', lookup_expr='icontains')
    age = filters.NumberFilter(field_name='age', lookup_expr='exact')
    sum = filters.NumberFilter(field_name='sum', lookup_expr='exact')
    alreadyPaid = filters.NumberFilter(field_name='alreadyPaid', lookup_expr='exact')
    status = filters.BooleanFilter(field_name='status', lookup_expr='exact')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    group = filters.CharFilter(field_name='group__name', lookup_expr='icontains')
    surname = filters.CharFilter(field_name='surname', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    course = filters.ChoiceFilter(choices=ChoiceEnum.Courses)
    course_format = filters.ChoiceFilter(choices=ChoiceEnum.CourseFormat)
    course_type = filters.ChoiceFilter(choices=ChoiceEnum.CourseType)
    manager = filters.CharFilter(field_name='manager__name', lookup_expr='icontains')
    start_date = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = OrderModel
        fields = (
            'id', 'name', 'surname', 'email', 'phone', 'age', 'course', 'course_format', 'course_type', 'sum', 'status',
            'alreadyPaid', 'group', 'manager', 'start_date', 'end_date')
