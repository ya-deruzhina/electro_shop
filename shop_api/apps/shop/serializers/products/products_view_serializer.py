from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField (read_only = True)
    name = serializers.CharField(max_length=25, required=False)
    model = serializers.CharField(max_length=200, required=False)
    launch_date = serializers.DateTimeField(required=False)
    created_at = serializers.DateTimeField(required=False)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance