from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.serializers import LeadSerializer
from blog.models import Post
from rest_framework import viewsets
# Create your views here.
@login_required
class LeadListCreate(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = LeadSerializer