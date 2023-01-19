from core.enums.choice_enum import CourseFormatChoice, CoursesChoice, CourseTypeChoice

from apps.orders.models import OrderModel

from django_filters import OrderingFilter
from django_filters import rest_framework as filters


class OrderFilter(filters.FilterSet):
    order_by_field = 'order'
    order = OrderingFilter(
        fields=(
            'name',
            'id',
            'surname',
            'email',
            'phone',
            'age',
            'course',
            'course_type',
            'course_format',
            'sum',
            'status',
            'alreadyPaid',
            'group',
            'created_at',
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
    course = filters.ChoiceFilter(choices=CoursesChoice.choices)
    course_format = filters.ChoiceFilter(choices=CourseFormatChoice.choices)
    course_type = filters.ChoiceFilter(choices=CourseTypeChoice.choices)
    manager = filters.CharFilter(field_name='manager__name', lookup_expr='icontains')
    start_date = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = OrderModel
        fields = (
            'id', 'name', 'surname', 'email', 'phone', 'age', 'course', 'course_format', 'course_type', 'sum', 'status',
            'alreadyPaid', 'group', 'manager', 'start_date', 'end_date')
