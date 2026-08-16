from rest_framework import serializers
from book_model import models


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Review
        fields = '__all__'
    

class BookListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # reviews = serializers.StringRelatedField(many=True, read_only=True)
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='reviewdetail')
    class Meta:
        model = models.BookList
        fields = "__all__"

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive")
        return value






    
    
    
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # published_date = serializers.DateField()
    # isbn = serializers.CharField(max_length=13)
    # pages = serializers.IntegerField()
    # cover_image = serializers.ImageField()
    # language = serializers.CharField(max_length=50)