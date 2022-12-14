from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def to_representation(self, instance):
        path, ext = instance.get_path_and_extension()
        data = super().to_representation(instance)
        data['image'] = {'path': path, 'formats': [ext, '.webp']}
        return data
