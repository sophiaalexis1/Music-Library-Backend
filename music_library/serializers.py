from rest_framework import serializers;
from .models import Songs;

class MusicLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['title', 'artist', 'album', 'release_date', 'genre']