from rest_framework import serializers

from .models import Hotel, Class, Travel


class  HotelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    rating = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    image = serializers.ImageField(required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if not representation['image']:
            representation['image'] = 'media/default.jpg'
        if request and representation['image']:
            representation['image'] = request.build_absolute_uri(representation['image'])
        return representation

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def validate_rating(self, rating):
        if rating > 5 or rating < 0:
            raise serializers.ValidationError('Reyting [0; 5] oraliqda bo\'lishi kerak')
        return rating


class ClassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def create(self, validated_data):
        return Class.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class TravelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    period_amount = serializers.IntegerField()
    period_unit = serializers.CharField(max_length=30)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    travel_class_id = serializers.IntegerField()
    hotel_id = serializers.IntegerField()

    def create(self, validated_data):
        return Travel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.period_amount = validated_data.get('period_amount', instance.period_amount)
        instance.period_unit = validated_data.get('period_unit', instance.period_unit)
        instance.price = validated_data.get('price', instance.price)
        instance.travel_class_id = validated_data.get('class_id', instance.travel_class_id)
        instance.hotel_id = validated_data.get('hotel_id', instance.hotel_id)
        instance.save()
        return instance
