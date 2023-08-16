from rest_framework import serializers;
from .models import Songs;

class MusicLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id','title', 'artist', 'album', 'release_date', 'genre']
    
    # song_by_id = serializers.IntegerField(write_only=True)