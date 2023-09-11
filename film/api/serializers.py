from rest_framework import serializers
from film.models import FilmModel, ActorModel


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = "__all__"

class FilmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        exclude = ('views_count',)


class ActorSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True)
    class Meta:
        model = ActorModel
        fields = "__all__"

class ActorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorModel
        fields = "__all__"