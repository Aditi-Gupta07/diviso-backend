from rest_framework import serializers
from .models import Bill

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id','image','raw_text','total_amount','created_at']
        read_only_fields = ['raw_text','total_amount','created_at']