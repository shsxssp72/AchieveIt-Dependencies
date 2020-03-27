from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

from .models import Personnel, Customers, ProjectId, BusinessField


class PersonnelSerializer(HyperlinkedModelSerializer):
    user_id = serializers.CharField()

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
    referred_coordinator_id = serializers.CharField()

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
        model = ProjectId
        fields = [
            'project_id',
        ]


class BusinessFieldSerializer(HyperlinkedModelSerializer):
    business_field_id = serializers.CharField()

    class Meta:
        model = BusinessField
        fields = [
            'business_field_id',
            'business_field_description',
        ]
