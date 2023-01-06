from rest_framework import serializers
from .models import Location, Episode, Character


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'world', 'description', 'image']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):
    character = serializers.StringRelatedField(many=True)

    class Meta:
        model = Episode
        fields = '__all__'


class CreateEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
