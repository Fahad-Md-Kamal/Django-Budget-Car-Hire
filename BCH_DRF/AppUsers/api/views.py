from rest_framework import generics, permissions
from StatusApp.serializers import BlogListSerializer
from CoreApp.models import Blog
    

class UserBlogListAPIView(generics.ListAPIView):
    pass
    serializer_class            = BlogListSerializer
    permission_classes          = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user             = self.request.user
        return Blog.objects.filter( user=user )
        