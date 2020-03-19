from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Personnel, Customers


class PersonnelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Personnel
        fields = [
            'user_id',
            'user_name',
            'user_email',
            'user_department',
            'user_telephone',
        ]


class CustomersSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = [
            'customer_id',
            'referred_coordinator_id',
            'corporation_name',
            'customer_level',
            'customer_email',
            'customer_telephone',
            'customer_address',
        ]


class ProjectIdSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = [
            'project_id',
        ]


class BusinessFieldSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = [
            'business_field_id',
            'business_field_description',
        ]
