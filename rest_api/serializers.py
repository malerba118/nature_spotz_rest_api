from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_api.models import Spot, Tip, Review, Photo, Favorite, ParkingLocation



class DynamicFieldsSerializerMixin(object):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsSerializerMixin, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(DynamicFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class TipSerializer(DynamicFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):

    spot = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tip
        fields = (
            "id",
            "spot",
            "tip",
            "created_at",
            "author",
        )
        read_only_fields = (
            "id",
            "spot",
            "created_at",
            "author",
        )


class ReviewSerializer(DynamicFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):

    spot = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "spot",
            "rating",
            "review",
            "created_at",
            "author"
        )
        read_only_fields = (
            "id",
            "spot",
            "created_at",
            "author",
        )


class ParkingLocationSerializer(DynamicFieldsSerializerMixin, GeoFeatureModelSerializer):

    spot = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ParkingLocation
        geo_field = "location"
        fields = (
            "spot",
            "location",
            "description",
            "created_at",
        )
        read_only_fields = (
            "spot",
            "created_at",
        )

class SpotSerializer(DynamicFieldsSerializerMixin, GeoFeatureModelSerializer):

    tips = TipSerializer(many=True, read_only=True, fields=("tip", "created_at"))

    reviews =  ReviewSerializer(many=True, read_only=True, fields=("rating", "review", "created_at"))

    additional_photos =  serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="photo-detail",
        lookup_field="pk"
    )

    parking_locations = ParkingLocationSerializer(many=True, read_only=True)

    # parking_locations = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="parking-location-detail",
    #     lookup_field="pk"
    # )

    class Meta:
        model = Spot
        geo_field = "location"
        fields = (
            "id",
            "title",
            "description",
            "family_safe",
            "skill_level",
            "danger_level",
            "feature_types",
            "activity_types",
            "primary_photo",
            "additional_photos",
            "tips",
            "reviews",
            "parking_locations",
        )


class PhotoSerializer(DynamicFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):

    spot = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Photo
        fields = (
            "id",
            "photo",
            "created_at",
            "spot",
        )
        read_only_fields = (
            "id",
            "spot",
            "created_at",
        )

class FavoriteSerializer(DynamicFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):

    spot = SpotSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = (
            "id",
            "user",
            "spot",
            "created_at",
        )

