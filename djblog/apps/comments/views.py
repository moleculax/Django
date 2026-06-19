from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Comment

def index(request):
    # Trae todos los comentarios con sus campos
    comments = Comment.objects.all().values(
        "id", "content", "created_at", "updated_at", "user_id", "post_id"
    )
    return JsonResponse(list(comments), safe=False)

