from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from blog.Serializer import PostSerializer


@csrf_exempt
def post_list(request):
    
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

   