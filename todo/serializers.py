from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


    def validate(self, attrs):
        title = attrs.get('title')
        print(title)
        title.upper()
        attrs['title']= title.upper()
        return attrs

    def validate_description(self, d):
        if len(d) < 20:
            raise serializers.ValidationError('слишком короткое описание')
        return d

