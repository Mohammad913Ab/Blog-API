from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'parent', 'replies', 'created_at']
        read_only_fields = ['user', 'replies']

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []

    def validate(self, data):
        parent = data.get('parent')
        if parent and parent.post != data.get('post'):
            raise serializers.ValidationError("Parent comment must belong to the same post.")
        return data

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'author',
            'category', 'category_id', 'is_published',
            'image', 'video',
            'created_at', 'updated_at', 'comments'
        ]

    def validate(self, data):
        image = data.get('image')
        video = data.get('video')
        if image and video:
            raise serializers.ValidationError("You can upload either an image or a video, not both.")
        elif not image and not video:
            raise serializers.ValidationError("You must upload either an image or a video.")
             
        return data