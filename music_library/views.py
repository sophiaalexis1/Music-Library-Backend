from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Songs
from .serializers import MusicLibrarySerializer


# Create your views here.

@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET':
        songs = Songs.objects.all()
        serializer = MusicLibrarySerializer(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST': 
        serializer = MusicLibrarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)