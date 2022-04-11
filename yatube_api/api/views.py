from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.mixins import ListCreateViewSet
from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
)
from posts.models import Post, Group


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)
        post_comments = post_obj.comments.all()
        return post_comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post_obj)


class GroupViewSet(ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (AllowAny,)


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
