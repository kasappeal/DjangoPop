from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ad
        fields = ['id', 'name', 'price', 'image']


class AdSerializer(AdListSerializer):

    class Meta(AdListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['owner']
