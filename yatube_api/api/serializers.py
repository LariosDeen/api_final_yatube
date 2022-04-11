from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from posts.models import User, Post, Comment, Group, Follow


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


# Привет, Екатерина. Не нашёл твой контакт в слаке, поэтому пишу здесь.
# Я ограничил методы в классе FollowViewSet.
# Каким родительским классом нужно ограничить методы в этом сериализаторе?
class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', read_only=True, default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны на этого автора.'
            )
        ]

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        if user == following:
            raise ValidationError('Вы не можете подписаться на самого себя.')
        return data
