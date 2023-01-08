from rest_framework import serializers
from note_api.models import NoteModel


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = '__all__'
        # fields = (
        #     'title',
        # )

        extra_kwargs = {
            'title': {'error_messages': {'blank': "Please provide a description"}},
        }
