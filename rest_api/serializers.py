from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_api.models import Spot, Tip, Review, Photo


class DynamicFieldsHLModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsHLModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class TipSerializer(DynamicFieldsHLModelSerializer):

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


class ReviewSerializer(DynamicFieldsHLModelSerializer):

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


class SpotSerializer(GeoFeatureModelSerializer):

    tips = TipSerializer(many=True, read_only=True, fields=("tip", "created_at"))

    reviews =  ReviewSerializer(many=True, read_only=True, fields=("rating", "review", "created_at"))

    additional_photos =  serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="photo-detail",
        lookup_field="pk"
    )

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
        )


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

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