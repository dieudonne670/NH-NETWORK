# feedback/serializers.py
from rest_framework import serializers
from .models import MTNFeedback, OrangeFeedback, CamtelFeedback, NexttelFeedback

class MTNFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MTNFeedback
        fields = '__all__'

class OrangeFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrangeFeedback
        fields = '__all__'

class CamtelFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamtelFeedback
        fields = '__all__'

class NexttelFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = NexttelFeedback
        fields = '__all__'
