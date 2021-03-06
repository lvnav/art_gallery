from api.models import Genre
from api.serializers.simple import SimplePaintingSerializer
from rest_framework import serializers


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    paintings = SimplePaintingSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
