from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import Link
from .serializers import LinkSerializer, RegisterSerializer
from .url_generator import generate_code
from django.shortcuts import render

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_short_link(request):
    serializer = LinkSerializer(data=request.data)
    if serializer.is_valid():
        original_url = serializer.validated_data['original_url']
        existing = Link.objects.filter(user=request.user, original_url=original_url).first()
        if existing:
            return Response(LinkSerializer(existing).data, status=status.HTTP_200_OK)
        code = generate_code()
        while Link.objects.filter(short_code=code).exists():
            code = generate_code()
        link = Link.objects.create(user=request.user, original_url=original_url, short_code=code)
        return Response(LinkSerializer(link).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_links(request):
    links = Link.objects.filter(user=request.user).order_by('-created_at')
    return Response(LinkSerializer(links, many=True).data)

@api_view(['GET'])
@permission_classes([AllowAny])
def redirect_to_original(request, code):
    link = get_object_or_404(Link, short_code=code)
    link.clicks += 1
    link.save()
    return redirect(link.original_url)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_link(request, code):
    link = get_object_or_404(Link, short_code=code, user=request.user)
    link.delete()
    return Response({"message": "Link deleted successfully"}, status=status.HTTP_200_OK)



def frontend(request):
    return render(request, 'index.html')
